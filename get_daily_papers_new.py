def get_daily_papers(topic, query="slam", max_results=2, domain_filters=None, final_max_results=None):
    """
    @param topic: str
    @param query: str
    @param domain_filters: list, 领域筛选关键词列表
    @param final_max_results: int, 最终要筛选的论文数量，如果为None则使用max_results
    @return paper_with_code: dict
    """
    # 如果没有指定最终目标数量，则使用max_results
    if final_max_results is None:
        final_max_results = max_results
    
    # output
    content = dict()
    content_to_web = dict()
    
    # 如果启用了领域筛选，使用循环持续获取直到达到目标数量
    if domain_filters:
        batch_size = 20  # 每次获取的论文数量
        max_iterations = 10  # 最大循环次数，防止无限循环
        total_fetched = 0  # 记录已获取的总论文数
        
        logging.info(f"Domain filtering enabled, target: {final_max_results} papers, batch size: {batch_size}")
        
        for iteration in range(max_iterations):
            if len(content) >= final_max_results:
                logging.info(f"Reached target of {final_max_results} papers, stopping search")
                break
            
            start_index = total_fetched
            end_index = start_index + batch_size
            
            logging.info(f"Iteration {iteration + 1}/{max_iterations}: fetching papers {start_index}-{end_index}")
            
            search_engine = arxiv.Search(
                query = query,
                max_results = end_index,
                sort_by = arxiv.SortCriterion.SubmittedDate
            )
            
            # 获取结果并跳过之前已经处理过的论文
            results = list(search_engine.results())
            results = results[start_index:]  # 只处理新获取的论文
            
            if not results:
                logging.info("No more papers available, stopping search")
                break
            
            matched_count = len(content)  # 记录当前匹配的论文数量
            new_papers_found = False
            
            for result in results:
                paper_id            = result.get_short_id()
                paper_title         = result.title
                paper_url           = result.entry_id
                paper_abstract      = result.summary.replace("\\n"," ")
                paper_authors       = get_authors(result.authors)
                paper_first_author  = get_authors(result.authors,first_author = True)
                primary_category    = result.primary_category
                publish_time        = result.published.date()
                update_time         = result.updated.date()
                comments            = result.comment

                logging.info(f"Time = {update_time} title = {paper_title} author = {paper_first_author}")

                # 二次筛选：检查论文标题是否包含领域关键词
                domain_match = False
                for keyword in domain_filters:
                    if keyword.lower() in paper_title.lower():
                        domain_match = True
                        break
                
                if not domain_match:
                    logging.info(f"Filtered out paper: {paper_title} (no domain keyword match)")
                    continue  # 跳过不匹配的论文
                
                new_papers_found = True
                
                # eg: 2108.09112v1 -> 2108.09112
                ver_pos = paper_id.find('v')
                if ver_pos == -1:
                    paper_key = paper_id
                else:
                    paper_key = paper_id[0:ver_pos]
                paper_url = arxiv_url + 'abs/' + paper_key

                # Since PapersWithCode API is deprecated, we no longer fetch code links
                # Papers will be listed without code links
                content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|null|\n".format(
                       update_time,paper_title,paper_first_author,paper_key,paper_url)
                content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({})".format(
                       update_time,paper_title,paper_first_author,paper_url,paper_url)

                # TODO: select useful comments
                comments = None
                if comments != None:
                    content_to_web[paper_key] += f", {comments}\n"
                else:
                    content_to_web[paper_key] += f"\n"

                # 如果已经达到目标数量，停止处理当前批次
                if len(content) >= final_max_results:
                    logging.info(f"Reached target of {final_max_results} papers, stopping")
                    break
            
            total_fetched = end_index
            
            # 如果这批次没有找到任何新论文，说明已经没有更多相关论文了
            if not new_papers_found:
                logging.info(f"No matching papers found in iteration {iteration + 1}, stopping search")
                break
            
            matched_count = len(content) - matched_count
            logging.info(f"Iteration {iteration + 1} found {matched_count} matching papers, total: {len(content)}/{final_max_results}")
        
        logging.info(f"Domain filtering complete: found {len(content)} papers matching domain criteria (target: {final_max_results})")
    else:
        # 不启用领域筛选时，直接获取指定数量的论文
        search_engine = arxiv.Search(
            query = query,
            max_results = max_results,
            sort_by = arxiv.SortCriterion.SubmittedDate
        )

        for result in search_engine.results():

            paper_id            = result.get_short_id()
            paper_title         = result.title
            paper_url           = result.entry_id
            paper_abstract      = result.summary.replace("\\n"," ")
            paper_authors       = get_authors(result.authors)
            paper_first_author  = get_authors(result.authors,first_author = True)
            primary_category    = result.primary_category
            publish_time        = result.published.date()
            update_time         = result.updated.date()
            comments            = result.comment

            logging.info(f"Time = {update_time} title = {paper_title} author = {paper_first_author}")

            # eg: 2108.09112v1 -> 2108.09112
            ver_pos = paper_id.find('v')
            if ver_pos == -1:
                paper_key = paper_id
            else:
                paper_key = paper_id[0:ver_pos]
            paper_url = arxiv_url + 'abs/' + paper_key

            # Since PapersWithCode API is deprecated, we no longer fetch code links
            # Papers will be listed without code links
            content[paper_key] = "|**{}**|**{}**|{} et.al.|[{}]({})|null|\n".format(
                   update_time,paper_title,paper_first_author,paper_key,paper_url)
            content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({})".format(
                   update_time,paper_title,paper_first_author,paper_url,paper_url)

            # TODO: select useful comments
            comments = None
            if comments != None:
                content_to_web[paper_key] += f", {comments}\n"
            else:
                content_to_web[paper_key] += f"\n"
        
        logging.info(f"Found {len(content)} papers (no domain filtering)")

    data = {topic:content}
    data_web = {topic:content_to_web}
    
    return data,data_web