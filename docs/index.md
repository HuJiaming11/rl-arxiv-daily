---
layout: default
---

<style>
  /* 控制整个页面的最大宽度，提升大屏幕阅读体验 */
  body {
    max-width: 2200px;
    margin: 0 auto;
    padding: 20px;
  }
  table {
    table-layout: fixed;
    width: 100%;
  }
  table th, table td {
    word-wrap: break-word;
    padding: 8px;
    vertical-align: top;
  }
  /* 根据表格列数（共6列）设置宽度比例 */
  table th:nth-child(1), table td:nth-child(1) { width: 5%; }  /* 发布日期 */
  table th:nth-child(2), table td:nth-child(2) { width: 15%; }  /* 标题 */
  table th:nth-child(3), table td:nth-child(3) { width: 10%; }  /* 作者 */
  table th:nth-child(4), table td:nth-child(4) { width: 5%; }   /* PDF */
  table th:nth-child(5), table td:nth-child(5) { width: 5%; }   /* 代码 */
  table th:nth-child(6), table td:nth-child(6) { width: 60%; }  /* 摘要（最后一列） */
</style>

## Updated on 2026.08.30
> Usage instructions: [here](./docs/README.md#usage)

## Reinforcement Learning

| Publish Date | Title | Authors | PDF | Code | 摘要 |
|:---------|:-----------------------|:---------|:------|:------|:-------------------------------------|
|**2026-08-27**|**Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation**|Wendong Li et.al.|[2608.27158](http://arxiv.org/abs/2608.27158)|null|<think> 好的，用户让我用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我需要仔细阅读用户提供的论文信息，提取关键点。  论文标题是关于机器人群体导航中的短时规划，问题在于现有强化学习方法只能输出单个反应动作，无法处理多样的短时避让策略。方法部分提到了PDPO框架，先用扩散策略预训练，再用PPO微调，生成五步动作块，并处理边界问题。结论是PDPO在成功率上优于基线，特别是处理修改后的边界基准测试时效果更好。  用户要求突出核心创新点，避免技术细节。我需要确保问题部分明确现有方法的不足，方法部分强调扩散策略和动作块，结论部分说明实验结果和改进点。同时要严格按照格式，不换行，不添加其他内容。  检查字数，确保不超过300字。可能需要精简语言，比如将“pretrained on collision-avoidance demonstrations”简化为“预训练于碰撞避让示教数据”，保持简洁。还要注意用户提到的边界问题处理，作为方法的一部分，用“将边界违反视为碰撞”来概括。  最后，确保所有内容在同一行，没有换行符，正确使用【】括号，不包含任何解释。现在组合起来，确认是否符合所有要求。 </think> 【问题】机器人群体导航需安全高效决策，现有强化学习方法单步反应动作无法表征多样短时避让策略，且易越界【方法】提出PDPO框架，预训练扩散策略生成五步动作块，结合PPO微调，将边界违反视为碰撞进行修正【结论】PDPO在成功率上优于基线，动作块对修改边界基准测试效果显著|
|**2026-08-27**|**GRAFT: Grounded and Efficient Online Reinforcement Adaptation for Fine-Grained Robot Manipulation**|Yibo Qiu et.al.|[2608.27079](http://arxiv.org/abs/2608.27079)|null|<think> 好的，我现在需要帮用户精简总结这篇名为GRAFT的论文，按照用户给的格式：问题、方法、结论，控制在300字以内。首先，我得仔细阅读用户提供的摘要，抓住核心内容。  问题部分，用户提到预训练的VLA策略在细粒度生物医学任务中在线适应困难，原因有两个：一是任务成功依赖细微的视觉线索，而任务级奖励无法指导视觉 grounding；二是在线适应受VLA推理和回放更新的计算成本限制。我需要把这些简化成问题，突出关键点，比如视觉 grounding 学习困难和计算开销。  接下来是方法，GRAFT的创新点有两个：区域级监督学习视点特定的视觉锚点，不需要区域提案；结合单步动作生成和缓存视觉语言前缀复用，加速学习。这里要避免技术细节，只说核心方法，比如“区域级监督”和“单步动作+缓存前缀”。  结论部分，用户提到在四个生物医学任务中，GRAFT提高了25%的成功率，同时减少计算开销。需要强调结果，比如“提升25%成功率”和“降低计算成本”。  然后检查格式，确保问题、方法、结论在同一行，用中文，无换行，总字数不超过300。可能需要调整用词，比如“细粒度生物医学任务在线适应困难”作为问题，方法部分用“区域级监督与单步动作缓存”来概括，结论部分突出成果。最后通读检查是否符合要求，确保没有多余的解释，核心创新点突出。 </think> 问题：预训练VLA策略在细粒度生物医学任务中在线适应困难，因视觉 grounding 学习受限于任务级奖励无法指导视觉关注区域和计算成本高；结论：GRAFT通过区域级监督与单步动作缓存实现25%成功率提升和计算开销降低。|
|**2026-08-26**|**$R^3$: Training Robots to Reason in Natural Language via Reinforcement Learning**|Lehong Wu et.al.|[2608.26053](http://arxiv.org/abs/2608.26053)|null|<think> 好的，我现在需要帮用户精简总结这篇论文，严格按照要求的格式，控制在300字以内。首先，我得仔细阅读用户提供的论文信息，确保理解核心内容。  论文标题是$R^3$: 训练机器人在自然语言中通过强化学习进行推理。摘要里提到，语言推理能帮助基础模型在测试时更高效处理复杂任务，比如分解问题、跟踪约束和预测后果。但不确定这种机制能否提升机器人操作效果，尤其是在长 hạn任务中需要跟踪部分进展、物体关系、纠正错误等。作者提出用$R^3$方法，将预训练的VLM（大语言模型）转化为机器人推理器，分两步：先中期训练VLM使用专家生成的推理痕迹，再通过单步评分强化学习优化，使用离线动作数据。与之前的方法不同，$R^3$使用自由形式的语言推理生成测试时的行动指导，而不是结构化痕迹。实验在Language Table和模拟双臂包装任务中进行，结果显示$R^3$在探索和泛化上优于传统方法，特别是优于仅用指令的模仿学习基线。结论是自由语言推理可作为测试时计算机制来引导底层策略。  接下来要按照用户的要求，分问题、方法、结论三部分，突出核心创新点，避免技术细节。用户强调要严格格式，所有内容在同一行，无换行符，无其他解释。需要检查字数是否在300字以内，同时确保每个部分的信息准确且简洁。  问题部分要说明研究目标，即验证VLM能否直接通过自然语言指导机器人操作，特别是在长 hạn任务中的效果。方法部分要概述$R^3$ 的两步训练流程，强调自由语言推理和离线数据优化。结论部分则要总结优势，如提升探索、泛化，超越基线，并指出自由语言推理的作用。  需要注意术语的准确性，比如“mid-train”翻译为中期训练，“rubric-based RL”可能译为评分强化学习。同时要确保不遗漏关键创新点，如对比之前结构化痕迹的方法，使用自由形式语言，以及实验结果的有效性。  最后检查格式是否符合要求，没有换行，用【】括号，用中文，字数控制。可能需要多次调整，确保每个部分的信息准确且简洁，同时符合用户的所有要求。 </think> 【问题】验证大语言|
|**2026-08-24**|**Reward-Free Continual Adaptation for Resilient Space Robots**|Andrej Orsula et.al.|[2608.23452](http://arxiv.org/abs/2608.23452)|null|<think> 好的，我现在需要帮用户精简总结这篇论文，按照要求的格式输出。首先，用户给了一个具体的结构：问题、方法、结论，每部分要简洁，总字数控制在300字以内，而且要突出核心创新点，避免技术细节。  首先看论文标题和摘要。标题是“Reward-Free Continual Adaptation for Resilient Space Robots”，核心在于不需要奖励的持续适应，针对空间机器人的硬件退化问题。摘要里提到传统控制策略在极端环境下容易出问题，因为硬件退化。而传统的持续强化学习需要奖励信号，但在太空环境中难以获得，因为缺乏外部追踪系统和环境复杂。所以问题应该是空间机器人面临硬件退化，传统控制策略失效，而持续强化学习需要奖励但无法获取。  接下来是方法部分。论文提出的方法是基于潜在状态世界模型的奖励-free 持续学习框架。他们先通过仿真预训练世界模型，学习奖励结构的预测。部署时冻结观察编码器和奖励预测器，只更新过渡动态，通过无监督回滚。然后训练策略完全基于更新的世界模型生成的想象轨迹，无需新奖励。核心创新点在于不需要奖励信号，利用预训练的世界模型在部署后更新动态，通过想象轨迹训练策略。  结论部分需要说明这种方法有效。论文展示了在模拟的行星 traversal、轨道导航和精密组装任务中，面对严重形态学故障，系统能够适应，证明了方法的有效性。  现在需要把这些内容浓缩到问题、方法、结论三个部分，每部分用简短的句子，避免技术细节。用户强调要严格按照格式，所有内容在同一行，无换行符，无其他解释。所以要注意字数和结构。  检查是否符合要求：问题部分要突出硬件退化导致传统控制失效，持续强化学习需要奖励但无法获取。方法部分强调预训练世界模型，冻结部分参数，无监督回滚，基于想象轨迹训练。结论部分说明在多个任务中有效，无需奖励适应退化。  最后确保总字数在300以内，可能需要调整用词，比如“硬件退化”可以简化为“硬件退化”，“无监督回滚”可能简化为“无监督更新”等。但用户要求突出核心创新点，所以关键点不能遗漏。比如“潜在状态世界模型”、“冻结观察编码器”、“奖励预测器”、“无监督回滚”、“想象轨迹”这些可能需要保留，但用更|
|**2026-08-24**|**Distributed Trajectory Planning and Resource Allocation for Dynamic Multi-UAV Collaborative Computing**|Tiankui Zhang et.al.|[2608.23123](http://arxiv.org/abs/2608.23123)|null|<think> 好的，我需要帮用户总结这篇论文，按照要求的格式，控制在300字以内，突出核心创新点，避免技术细节。首先，我得仔细阅读用户提供的论文摘要，提取关键信息。  问题部分应该包括动态多无人机协作中的计算资源分配和路径规划挑战，以及如何平衡各方利益。方法部分需要提到基于Stackelberg博弈的分层优化算法，使用MADRL框架，特别是MAPPO和两阶段迭代算法。结论部分要强调效率提升，比如无人机效率提高18.58%，终端开销降低33.77%，还有动态参与下的稳定收敛。  要注意用户强调不要技术细节，所以像具体算法名称可能需要简化，但用户给的例子中用了MAPPO，所以可能需要保留。同时要确保各部分字数精简，符合格式要求，同一行内，无换行，不包含其他解释。需要检查字数是否在300以内，可能需要调整用词，比如“动态多无人机协作”改为“动态多-UAV协作”更准确。最后确保严格按照问题、方法、结论的顺序，每个部分用【】括起，中间用空格分隔，没有标点错误。 </think> 【问题】动态多-UAV协作中计算资源分配与路径规划协同优化及多方利益平衡问题【方法】提出基于Stackelberg博弈的分层MADRL算法，领导者层通过MAPPO优化轨迹规划、任务迁移、终端关联与定价，跟随者层采用两阶段迭代优化卸载策略【结论】实现18.58%无人机效率提升与33.77%终端开销降低，支持动态规模下的稳定收敛与资源利用率优化|
|**2026-08-21**|**Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning**|Varun Giridhar et.al.|[2608.21204](http://arxiv.org/abs/2608.21204)|null|<think> 好的，我需要帮用户总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内，并且突出核心创新点，避免技术细节。首先，我得仔细阅读用户提供的论文摘要和具体要求。  论文标题是“Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning”。摘要里提到，行为克隆（BC）虽然有效，但无法自我改进，因为失败无法学习，而强化学习微调又难以处理大型模型。他们提出了Q-Planning，给大的视觉运动BC政策配一个小的离线Q函数。Q函数可以估计值而不是模仿动作，能同时训练成功示范和失败部署，BC不行。利用这个不对称性，在推理时用Q加权平均选择动作，在线自我改进时只微调Q函数，保持BC权重不变。实验结果显示在多个任务中性能提升显著，尤其是真实机器人任务。  现在要总结成问题、方法、结论三个部分，每部分一句话，总共不超过300字。核心创新点应该是Q-Planning结合离线Q函数和BC，利用价值引导和仅微调Q的自适应改进。需要避免技术细节，比如具体的实验平台或参数设置。  问题部分要说明BC的局限性，无法自我改进，依赖人类示范。方法部分强调Q-Planning的结构和优势，离线Q函数训练和在线微调。结论部分突出性能提升，特别是真实机器人任务，稳定改进。要确保每部分简洁，直接，符合用户格式要求，同一行内无换行，不包含其他解释。现在检查是否符合字数，可能需要调整用词，比如“离线Q函数”可以简化为“离线Q值学习”等。确保每个部分不超过太长，整体控制在300字以内。 </think> 问题：行为克隆（BC）因无法通过失败数据自我改进且强化学习微调难以适配大型模型而受限；方法：提出Q-Planning框架，通过离线Q值学习与BC政策协同，利用Q函数吸收成功示范和失败部署数据，仅在线微调Q值实现自适应改进；结论：该方法在多个机器人任务中显著提升性能（LIBERO-10达99%，RoboTwin达91.4%），且在真实接触任务中无需人工干预实现持续优化（stack-cups达90%，insert-wallet达80%），稳定优于S|
|**2026-08-21**|**Teaching is a Process: The TOSS Framework for Modeling Human Teaching Decisions in Human-Interactive Robot Learning**|Bernhard Hilpert et.al.|[2608.21083](http://arxiv.org/abs/2608.21083)|null|<think> 好的，我现在需要帮用户总结这篇论文，按照他们给的格式：问题、方法、结论，控制在300字以内，还要突出核心创新点，避免技术细节。首先，我得仔细阅读论文的摘要，抓住关键点。  论文标题提到TOSS框架，问题应该是人类与机器人教学中的意图对齐问题。摘要里说成功的人机教学需要机器人处理需求和人类教学意图对齐，但如何理解这种对齐呢？作者通过研究人类在RL场景中的教学行为，发现了TOSS框架。核心创新点应该就是TOSS框架本身，以及它如何模型化教学决策。  接下来，问题部分需要简洁说明当前的对齐问题，方法部分要提到他们用了34名参与者，观察两个RL场景，分析教学响应，提炼出TOSS的四个要素：触发器、目标、信号、策略。结论部分则是TOSS框架的应用价值，比如提供数据集、理论基础，用于理解教学决策、模拟导师和设计教学环境。  要注意用户要求不要技术细节，所以不需要深入每个要素的具体内容，而是强调框架的结构和整体贡献。同时要确保各部分字数均衡，总字数不超过300。检查格式是否严格按照问题、方法、结论排列，同一行内无换行，没有其他解释。最后确认核心创新点是否突出，即TOSS框架的提出和其应用价值。 </think> 问题：人机交互中机器人学习需求与人类教学意图对齐不足导致教学效率受限；方法：通过34人观察实验分析204次教学行为，提炼TOSS框架（触发器-信号响应受目标-策略调制）；结论：TOSS为教学决策建模提供理论框架，支持教学模拟算法优化和教学场景设计，突破传统机器人学习约束。|
|**2026-08-20**|**RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement Learning in Robotic Manipulation**|Shaoxuan Wang et.al.|[2608.20208](http://arxiv.org/abs/2608.20208)|null|
|**2026-08-20**|**Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving**|Mehdi Azarafza et.al.|[2608.20129](http://arxiv.org/abs/2608.20129)|null|
|**2026-08-18**|**tinyDSM: A Framework for Skill Modeling and Development for Resource-Constrained Millirobots**|Markus D. Kobelrausch et.al.|[2608.17596](http://arxiv.org/abs/2608.17596)|null|
|**2026-08-18**|**Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation**|Hongyan Feng et.al.|[2608.17512](http://arxiv.org/abs/2608.17512)|null|
|**2026-08-17**|**HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL**|Langzhe Gu et.al.|[2608.16837](http://arxiv.org/abs/2608.16837)|null|
|**2026-08-17**|**The Ethical Decision Head: Operationalizing Normative Ethics in Autonomous Vehicles via Reinforcement Learning from Human Feedback**|Thomas Mbrice et.al.|[2608.16710](http://arxiv.org/abs/2608.16710)|null|
|**2026-08-13**|**FIRE-VLA: Failure-Informed Self-Evolution for Vision-Language-Action Models in Autonomous Driving**|Hao Dou et.al.|[2608.13395](http://arxiv.org/abs/2608.13395)|null|
|**2026-08-06**|**Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation**|He Kong et.al.|[2608.05999](http://arxiv.org/abs/2608.05999)|null|
|**2026-08-04**|**GORDON: Graph-based Object-centric Rewards for Decomposition of Long-Horizon Manipulation**|Andrea Protopapa et.al.|[2608.03753](http://arxiv.org/abs/2608.03753)|null|
|**2026-08-02**|**RL Bootstrapping of OpenVLA-OFT for a Novel Robot Embodiment**|Damir Nurtdinov et.al.|[2608.01013](http://arxiv.org/abs/2608.01013)|null|
|**2026-08-01**|**Minute-Scale Training for Microrobot Navigation**|Yinghan Sun et.al.|[2608.00854](http://arxiv.org/abs/2608.00854)|null|
|**2026-07-31**|**CLIFT: Turning Gemini Robotics On-Device into Humanoid Specialists via Non-Invasive Closed-Loop Iterative Fine-Tuning**|Yuxin Chen et.al.|[2607.29172](http://arxiv.org/abs/2607.29172)|null|
|**2026-07-30**|**MARS-RA: Rank Aggregation for Credit Assignment via Multimodal Comparisons in Embodied Multi-Agent Cooperation**|Dawei Wang et.al.|[2607.27967](http://arxiv.org/abs/2607.27967)|null|
|**2026-07-30**|**Learning Social Robot Navigation By Sensing Human Legs**|Alberto Vaglio et.al.|[2607.27922](http://arxiv.org/abs/2607.27922)|null|
|**2026-07-29**|**SymmGrid: Super-Scaling On-Robot Learning with Parallelized Symmetries and Egocentric-Exocentric Visual Perception**|Gabe Everett et.al.|[2607.26985](http://arxiv.org/abs/2607.26985)|null|
|**2026-07-29**|**RLMM-Flow: A Flow-based Mobile Manipulation Framework with Latent-Space Reinforcement Learning**|Shuhang Wang et.al.|[2607.26460](http://arxiv.org/abs/2607.26460)|null|
|**2026-07-23**|**Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections**|Gil Lifshits et.al.|[2607.21488](http://arxiv.org/abs/2607.21488)|null|
|**2026-07-22**|**Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning**|Nicolas Kosanovic et.al.|[2607.20399](http://arxiv.org/abs/2607.20399)|null|
|**2026-07-20**|**Importance Sampling and PCA for Finding Failures in Commercial Autonomous Vehicles**|Hailey Warner et.al.|[2607.18106](http://arxiv.org/abs/2607.18106)|null|
|**2026-07-17**|**Data and Learning Where it Matters for Contact-Rich Manipulation**|Oliver Hausdörfer et.al.|[2607.15982](http://arxiv.org/abs/2607.15982)|null|
|**2026-07-16**|**WorkDrive: Roadwork Chain of Causation for Autonomous Driving**|Tianyi Jiang et.al.|[2607.14727](http://arxiv.org/abs/2607.14727)|null|
|**2026-07-13**|**Robust In-Hand Manipulation via Priors in Reinforcement Learning and Mechanical Design**|Yifei Chen et.al.|[2607.12105](http://arxiv.org/abs/2607.12105)|null|
|**2026-07-13**|**A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation**|Yunhai Feng et.al.|[2607.11874](http://arxiv.org/abs/2607.11874)|null|
|**2026-07-10**|**Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning**|Guanquan Wang et.al.|[2607.09336](http://arxiv.org/abs/2607.09336)|null|
|**2026-07-07**|**LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation**|Xinye Yang et.al.|[2607.06323](http://arxiv.org/abs/2607.06323)|null|
|**2026-07-07**|**Can Reinforcement Learning Efficiently Discover Price Manipulation?**|Ioanna-Yvonni Tsaknaki et.al.|[2607.06121](http://arxiv.org/abs/2607.06121)|null|
|**2026-07-06**|**Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning**|Matthew Foutter et.al.|[2607.04681](http://arxiv.org/abs/2607.04681)|null|
|**2026-07-06**|**PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving**|Pin Tang et.al.|[2607.04637](http://arxiv.org/abs/2607.04637)|null|
|**2026-07-05**|**A Perception-Manipulation Robotics System for Food Cutting**|Xinyuan Luo et.al.|[2607.04367](http://arxiv.org/abs/2607.04367)|null|
|**2026-07-02**|**EAGLE-360: Embodied Active Global-to-Local Exploration in 360 $^\circ$**|Jingtao Xu et.al.|[2607.02479](http://arxiv.org/abs/2607.02479)|null|
|**2026-07-02**|**WorldSample: Closed-loop Real-robot RL with World Modelling**|Yuquan Xue et.al.|[2607.02431](http://arxiv.org/abs/2607.02431)|null|
|**2026-07-02**|**Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning**|Satoshi Yamamori et.al.|[2607.02205](http://arxiv.org/abs/2607.02205)|null|
|**2026-06-30**|**OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation**|Arnav Balaji et.al.|[2606.31993](http://arxiv.org/abs/2606.31993)|null|
|**2026-06-30**|**Adapting Generalist Robot Policies with Semantic Reinforcement Learning**|Jagdeep Singh Bhatia et.al.|[2606.31958](http://arxiv.org/abs/2606.31958)|null|
|**2026-06-30**|**CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations**|Bowen Jiang et.al.|[2606.31909](http://arxiv.org/abs/2606.31909)|null|
|**2026-06-30**|**Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot**|Ethan Marot et.al.|[2606.31807](http://arxiv.org/abs/2606.31807)|null|
|**2026-06-26**|**Learning Stable In-Grasp Manipulation in a Non-Dropping Action Space**|Ha Thang Long Doan et.al.|[2606.28196](http://arxiv.org/abs/2606.28196)|null|
|**2026-06-26**|**PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation**|Peiwen Zhang et.al.|[2606.28128](http://arxiv.org/abs/2606.28128)|null|
|**2026-06-26**|**PPO-EAL: Exact Augmented Lagrangian Proximal Policy Optimization for Safe Robotic Control**|Jiatao Ding et.al.|[2606.27861](http://arxiv.org/abs/2606.27861)|null|
|**2026-06-25**|**VibeAct: Vibration to Actions for Contact-Rich Reactive Robot Dexterity**|Yuemin Mao et.al.|[2606.27344](http://arxiv.org/abs/2606.27344)|null|
|**2026-06-25**|**RobOralScan: Learning Active Intraoral Scanning for Robotic Dental Reconstruction**|Jinhyung Lee et.al.|[2606.26955](http://arxiv.org/abs/2606.26955)|null|
|**2026-06-24**|**Deep Reinforcement Learning-Enhanced Event-Triggered Data-Driven Predictive Control for a 3D Cable-Driven Soft Robotic Arm**|Cheng Ouyang et.al.|[2606.26048](http://arxiv.org/abs/2606.26048)|null|
|**2026-06-24**|**Learning Robot Visual Navigation in Crowds via Intention-Aware Scene Representations**|Han Bao et.al.|[2606.26047](http://arxiv.org/abs/2606.26047)|null|
|**2026-06-24**|**StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots**|Xincheng Tang et.al.|[2606.25765](http://arxiv.org/abs/2606.25765)|null|
|**2026-06-23**|**NoContactNoWorries: Estimating Contact through Vision and Proprioception for In-Hand Dexterous Manipulation**|Soham Patil et.al.|[2606.24450](http://arxiv.org/abs/2606.24450)|null|
|**2026-06-21**|**Scalable Multi-Task Data Generation via Reinforcement Learning for Language-Conditioned Bimanual Dexterous Manipulation**|Zechu Li et.al.|[2606.22471](http://arxiv.org/abs/2606.22471)|null|
|**2026-06-21**|**FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation**|Kexin Shi et.al.|[2606.22303](http://arxiv.org/abs/2606.22303)|null|
|**2026-06-18**|**Generating Robot Hands from Human Demonstrations**|Sha Yi et.al.|[2606.20549](http://arxiv.org/abs/2606.20549)|null|
|**2026-06-18**|**A Neuromorphic Reinforcement Learning Framework for Efficient Pathfinding in Robotic Mobile Fulfillment Systems**|Junzhe Xu et.al.|[2606.20031](http://arxiv.org/abs/2606.20031)|null|
|**2026-06-16**|**WireCraft: A Simulation Benchmark for Industrial DLO Manipulation**|Chongyu Zhu et.al.|[2606.18097](http://arxiv.org/abs/2606.18097)|null|
|**2026-06-15**|**VENOM: Versatile Embodied Network for Omni-bodied Motion tracking**|Siddharth Padmanabhan et.al.|[2606.16696](http://arxiv.org/abs/2606.16696)|null|
|**2026-06-15**|**Reinforcement Learning with Inner-loop Dynamics Estimator for Aerial Manipulation under Uncertainty**|Shivansh Pratap Singh et.al.|[2606.16621](http://arxiv.org/abs/2606.16621)|null|
|**2026-06-12**|**AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition**|Jixuan Chen et.al.|[2606.14674](http://arxiv.org/abs/2606.14674)|null|
|**2026-06-12**|**Kine2Go: Kinematic dataset for the Unitree Go2 robot with diverse gaits and motions**|Władysław Pałucki et.al.|[2606.14433](http://arxiv.org/abs/2606.14433)|null|
|**2026-06-12**|**Robust Fall Recovery for Armless Bipedal-Wheeled Robots Via Force-Guided Learning**|Haidong Hou et.al.|[2606.14270](http://arxiv.org/abs/2606.14270)|null|
|**2026-06-11**|**Mana: Dexterous Manipulation of Articulated Tools**|Zhao-Heng Yin et.al.|[2606.13677](http://arxiv.org/abs/2606.13677)|null|
|**2026-06-11**|**Improving Robotic Generalist Policies via Flow Reversal Steering**|Andy Tang et.al.|[2606.13675](http://arxiv.org/abs/2606.13675)|null|
|**2026-06-10**|**DrivingAgent: Design and Scheduling Agents for Autonomous Driving Systems**|Zhongyu Xia et.al.|[2606.12236](http://arxiv.org/abs/2606.12236)|null|
|**2026-06-05**|**Rapid co-design of Buoyancy-assisted robots for Challenging Locomotion using Gaussian Evolutionary Specialists**|Ankit Sinha et.al.|[2606.07424](http://arxiv.org/abs/2606.07424)|null|
|**2026-06-04**|**MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation**|Ilyass Taouil et.al.|[2606.06139](http://arxiv.org/abs/2606.06139)|null|
|**2026-06-04**|**L-SDPPO: Policy Optimization of Spiking Diffusion Policy for Intra-vehicular Robotic Manipulation**|Liwen Zhang et.al.|[2606.06049](http://arxiv.org/abs/2606.06049)|null|
|**2026-05-29**|**Batched Differentiable Rigid Body Dynamics in PyTorch for GPU-Accelerated Robot Learning**|Yue Wang et.al.|[2605.31481](http://arxiv.org/abs/2605.31481)|null|
|**2026-05-27**|**Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation**|Jiahe Pan et.al.|[2605.28812](http://arxiv.org/abs/2605.28812)|null|
|**2026-05-27**|**SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving**|Kangyu Wu et.al.|[2605.28583](http://arxiv.org/abs/2605.28583)|null|
|**2026-05-22**|**Robotic Strawberry Harvesting with Robust Vision and Deep Reinforcement Learning based Sim-to-Real Control**|Al Bashir et.al.|[2605.23863](http://arxiv.org/abs/2605.23863)|null|
|**2026-05-20**|**roto 2.0: The Robot Tactile Olympiad**|Elle Miller et.al.|[2605.21429](http://arxiv.org/abs/2605.21429)|null|
|**2026-05-20**|**Learning Robust Dexterous In-Hand Manipulation from Joint Sensors with Proprioceptive Transformer**|Senlan Yao et.al.|[2605.21330](http://arxiv.org/abs/2605.21330)|null|
|**2026-05-19**|**RoHIL: Robust Human-in-the-Loop Robotic Reinforcement Learning Against Illumination Variations**|Shuoqin Zhang et.al.|[2605.19924](http://arxiv.org/abs/2605.19924)|null|
|**2026-05-19**|**Beyond Action Residuals: Real-World Robot Policy Steering via Bottleneck Latent Reinforcement Learning**|Dongjie Yu et.al.|[2605.19919](http://arxiv.org/abs/2605.19919)|null|
|**2026-05-13**|**RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data**|Harold Haodong Chen et.al.|[2605.13775](http://arxiv.org/abs/2605.13775)|null|
|**2026-05-13**|**Robot Squid Game: Quadrupedal Locomotion for Traversing Narrow Tunnels**|Amir Hossain Raj et.al.|[2605.13665](http://arxiv.org/abs/2605.13665)|null|
|**2026-05-11**|**Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation**|Zhixuan Shen et.al.|[2605.10118](http://arxiv.org/abs/2605.10118)|null|
|**2026-05-11**|**Beyond Self-Play and Scale: A Behavior Benchmark for Generalization in Autonomous Driving**|Aron Distelzweig et.al.|[2605.10034](http://arxiv.org/abs/2605.10034)|null|
|**2026-05-08**|**123D: Unifying Multi-Modal Autonomous Driving Data at Scale**|Daniel Dauner et.al.|[2605.08084](http://arxiv.org/abs/2605.08084)|null|
|**2026-05-08**|**Active Embodiment Identification with Reinforcement Learning for Legged Robots**|Nico Bohlinger et.al.|[2605.08020](http://arxiv.org/abs/2605.08020)|null|
|**2026-05-05**|**SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision**|Shiyi Chen et.al.|[2605.03846](http://arxiv.org/abs/2605.03846)|null|
|**2026-05-05**|**SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems**|Yibang Tang et.al.|[2605.03842](http://arxiv.org/abs/2605.03842)|null|
|**2026-05-05**|**RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models**|Hao Wu et.al.|[2605.03821](http://arxiv.org/abs/2605.03821)|null|
|**2026-05-04**|**Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters**|Lingxiao Kong et.al.|[2605.02867](http://arxiv.org/abs/2605.02867)|null|
|**2026-05-01**|**Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies**|Yi Wang et.al.|[2605.00416](http://arxiv.org/abs/2605.00416)|null|
|**2026-04-29**|**ATLAS: An Annotation Tool for Long-horizon Robotic Action Segmentation**|Sergej Stanovcic et.al.|[2604.26637](http://arxiv.org/abs/2604.26637)|null|
|**2026-04-28**|**KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning**|Yixuan Huang et.al.|[2604.25788](http://arxiv.org/abs/2604.25788)|null|
|**2026-04-23**|**X2-N: A Transformable Wheel-legged Humanoid Robot with Dual-mode Locomotion and Manipulation**|Yan Ning et.al.|[2604.21541](http://arxiv.org/abs/2604.21541)|null|
|**2026-04-23**|**Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot**|Yucheng Xin et.al.|[2604.21351](http://arxiv.org/abs/2604.21351)|null|
|**2026-04-14**|**Tree Learning: A Multi-Skill Continual Learning Framework for Humanoid Robots**|Yifei Yan et.al.|[2604.12909](http://arxiv.org/abs/2604.12909)|null|
|**2026-04-14**|**A hierarchical spatial-aware algorithm with efficient reinforcement learning for human-robot task planning and allocation in production**|Jintao Xue et.al.|[2604.12669](http://arxiv.org/abs/2604.12669)|null|
|**2026-04-14**|**Safe reinforcement learning with online filtering for fatigue-predictive human-robot task planning and allocation in production**|Jintao Xue et.al.|[2604.12667](http://arxiv.org/abs/2604.12667)|null|
|**2026-04-14**|**FeaXDrive: Feasibility-aware Trajectory-Centric Diffusion Planning for End-to-End Autonomous Driving**|Baoyun Wang et.al.|[2604.12656](http://arxiv.org/abs/2604.12656)|null|
|**2026-04-14**|**A Comparison of Reinforcement Learning and Optimal Control Methods for Path Planning**|Qiang Le et.al.|[2604.12628](http://arxiv.org/abs/2604.12628)|null|
|**2026-04-14**|**Whole-Body Mobile Manipulation using Offline Reinforcement Learning on Sub-optimal Controllers**|Snehal Jauhri et.al.|[2604.12509](http://arxiv.org/abs/2604.12509)|null|
|**2026-04-14**|**A Heterogeneous Dual-Network Framework for Emergency Delivery UAVs: Communication Assurance and Path Planning Coordination**|Ping Huang et.al.|[2604.12501](http://arxiv.org/abs/2604.12501)|null|
|**2026-04-11**|**MoRI: Mixture of RL and IL Experts for Long-Horizon Manipulation Tasks**|Yaohang Xu et.al.|[2604.10165](http://arxiv.org/abs/2604.10165)|null|
|**2026-04-10**|**Learning Vision-Language-Action World Models for Autonomous Driving**|Guoqing Wang et.al.|[2604.09059](http://arxiv.org/abs/2604.09059)|null|
|**2026-04-09**|**LAMP: Lift Image-Editing as General 3D Priors for Open-world Manipulation**|Jingjing Wang et.al.|[2604.08475](http://arxiv.org/abs/2604.08475)|null|
|**2026-04-09**|**HiRO-Nav: Hybrid ReasOning Enables Efficient Embodied Navigation**|He Zhao et.al.|[2604.08232](http://arxiv.org/abs/2604.08232)|null|
|**2026-04-09**|**ViVa: A Video-Generative Value Model for Robot Reinforcement Learning**|Jindi Lv et.al.|[2604.08168](http://arxiv.org/abs/2604.08168)|null|
|**2026-04-09**|**On-Policy Distillation of Language Models for Autonomous Vehicle Motion Planning**|Amirhossein Afsharrad et.al.|[2604.07944](http://arxiv.org/abs/2604.07944)|null|
|**2026-04-09**|**RoboAgent: Chaining Basic Capabilities for Embodied Task Planning**|Peiran Xu et.al.|[2604.07774](http://arxiv.org/abs/2604.07774)|null|
|**2026-04-08**|**Robots that learn to evaluate models of collective behavior**|Mathis Hocke et.al.|[2604.07303](http://arxiv.org/abs/2604.07303)|null|
|**2026-04-08**|**Learning-Based Strategy for Composite Robot Assembly Skill Adaptation**|Khalil Abuibaid et.al.|[2604.06949](http://arxiv.org/abs/2604.06949)|null|
|**2026-04-08**|**Sustainable Transfer Learning for Adaptive Robot Skills**|Khalil Abuibaid et.al.|[2604.06943](http://arxiv.org/abs/2604.06943)|null|
|**2026-04-08**|**Train-Small Deploy-Large: Leveraging Diffusion-Based Multi-Robot Planning**|Siddharth Singh et.al.|[2604.06598](http://arxiv.org/abs/2604.06598)|null|
|**2026-04-06**|**FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control**|Donghu Kim et.al.|[2604.04539](http://arxiv.org/abs/2604.04539)|null|
|**2026-04-05**|**VA-FastNavi-MARL: Real-Time Robot Control with Multimedia-Driven Meta-Reinforcement Learning**|Yang Zhang et.al.|[2604.03998](http://arxiv.org/abs/2604.03998)|null|
|**2026-04-04**|**Drift-Based Policy Optimization: Native One-Step Policy Learning for Online Robot Control**|Yuxuan Gao et.al.|[2604.03540](http://arxiv.org/abs/2604.03540)|null|
|**2026-04-04**|**Optimizing Neurorobot Policy under Limited Demonstration Data through Preference Regret**|Viet Dung Nguyen et.al.|[2604.03523](http://arxiv.org/abs/2604.03523)|null|
|**2026-04-03**|**Sim2Real-AD: A Modular Sim-to-Real Framework for Deploying VLM-Guided Reinforcement Learning in Real-World Autonomous Driving**|Zilin Huang et.al.|[2604.03497](http://arxiv.org/abs/2604.03497)|null|
|**2026-04-03**|**ARM: Advantage Reward Modeling for Long-Horizon Manipulation**|Yiming Mao et.al.|[2604.03037](http://arxiv.org/abs/2604.03037)|null|
|**2026-04-03**|**Learning Locomotion on Complex Terrain for Quadrupedal Robots with Foot Position Maps and Stability Rewards**|Matthew Hwang et.al.|[2604.02744](http://arxiv.org/abs/2604.02744)|null|
|**2026-04-03**|**ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving**|Zihao Sheng et.al.|[2604.02714](http://arxiv.org/abs/2604.02714)|null|
|**2026-04-03**|**Beyond Semantic Manipulation: Token-Space Attacks on Reward Models**|Yuheng Zhang et.al.|[2604.02686](http://arxiv.org/abs/2604.02686)|null|
|**2026-04-02**|**Tune to Learn: How Controller Gains Shape Robot Policy Learning**|Antonia Bronars et.al.|[2604.02523](http://arxiv.org/abs/2604.02523)|null|
|**2026-04-02**|**Bridging Discrete Planning and Continuous Execution for Redundant Robot**|Teng Yan et.al.|[2604.02021](http://arxiv.org/abs/2604.02021)|null|
|**2026-04-01**|**Deep Reinforcement Learning for Robotic Manipulation under Distribution Shift with Bounded Extremum Seeking**|Shaifalee Saxena et.al.|[2604.01142](http://arxiv.org/abs/2604.01142)|null|
|**2026-03-31**|**Generalizable Dense Reward for Long-Horizon Robotic Tasks**|Silong Yong et.al.|[2604.00055](http://arxiv.org/abs/2604.00055)|null|
|**2026-03-31**|**Hybrid Framework for Robotic Manipulation: Integrating Reinforcement Learning and Large Language Models**|Md Saad et.al.|[2603.30022](http://arxiv.org/abs/2603.30022)|null|
|**2026-03-30**|**SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning**|Philip Schroeder et.al.|[2603.28730](http://arxiv.org/abs/2603.28730)|null|
|**2026-03-30**|**Critic-Free Deep Reinforcement Learning for Maritime Coverage Path Planning on Irregular Hexagonal Grids**|Carlos S. Sepúlveda et.al.|[2603.28385](http://arxiv.org/abs/2603.28385)|null|
|**2026-03-30**|**CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence**|Tianle Zeng et.al.|[2603.28032](http://arxiv.org/abs/2603.28032)|null|
|**2026-03-30**|**Flip Stunts on Bicycle Robots using Iterative Motion Imitation**|Jeonghwan Kim et.al.|[2603.27944](http://arxiv.org/abs/2603.27944)|null|
|**2026-04-01**|**D-SPEAR: Dual-Stream Prioritized Experience Adaptive Replay for Stable Reinforcement Learning in Robotic Manipulation**|Yu Zhang et.al.|[2603.27346](http://arxiv.org/abs/2603.27346)|null|
|**2026-04-01**|**Where-to-Learn: Analytical Policy Gradient Directed Exploration for On-Policy Robotic Reinforcement Learning**|Leixin Chang et.al.|[2603.27317](http://arxiv.org/abs/2603.27317)|null|
|**2026-03-31**|**Neuro-Cognitive Reward Modeling for Human-Centered Autonomous Vehicle Control**|Zhuoli Zhuang et.al.|[2603.25968](http://arxiv.org/abs/2603.25968)|null|
|**2026-03-26**|**Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning**|Jai Bardhan et.al.|[2603.25685](http://arxiv.org/abs/2603.25685)|null|
|**2026-03-26**|**Modernising Reinforcement Learning-Based Navigation for Embodied Semantic Scene Graph Generation**|Roman Kueble et.al.|[2603.25415](http://arxiv.org/abs/2603.25415)|null|
|**2026-03-26**|**Integrating Deep RL and Bayesian Inference for ObjectNav in Mobile Robotics**|João Castelo-Branco et.al.|[2603.25366](http://arxiv.org/abs/2603.25366)|null|
|**2026-03-26**|**Distributed Real-Time Vehicle Control for Emergency Vehicle Transit: A Scalable Cooperative Method**|WenXi Wang et.al.|[2603.25000](http://arxiv.org/abs/2603.25000)|null|
|**2026-03-26**|**COIN: Collaborative Interaction-Aware Multi-Agent Reinforcement Learning for Self-Driving Systems**|Yifeng Zhang et.al.|[2603.24931](http://arxiv.org/abs/2603.24931)|null|
|**2026-03-25**|**DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving**|Pengxuan Yang et.al.|[2603.24587](http://arxiv.org/abs/2603.24587)|null|
|**2026-03-25**|**Knowledge-Guided Manipulation Using Multi-Task Reinforcement Learning**|Aditya Narendra et.al.|[2603.24083](http://arxiv.org/abs/2603.24083)|null|
|**2026-03-24**|**Learning Multi-Agent Local Collision-Avoidance for Collaborative Carrying tasks with Coupled Quadrupedal Robots**|Francesca Bray et.al.|[2603.23278](http://arxiv.org/abs/2603.23278)|null|
|**2026-03-24**|**Path Planning and Reinforcement Learning-Driven Control of On-Orbit Free-Flying Multi-Arm Robots**|Álvaro Belmonte-Baeza et.al.|[2603.23182](http://arxiv.org/abs/2603.23182)|null|
|**2026-03-24**|**Grounding Sim-to-Real Generalization in Dexterous Manipulation: An Empirical Study with Vision-Language-Action Models**|Ruixing Jin et.al.|[2603.22876](http://arxiv.org/abs/2603.22876)|null|
|**2026-03-23**|**CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation**|Max Fu et.al.|[2603.22435](http://arxiv.org/abs/2603.22435)|null|
|**2026-03-23**|**DexDrummer: In-Hand, Contact-Rich, and Long-Horizon Dexterous Robot Drumming**|Hung-Chieh Fang et.al.|[2603.22263](http://arxiv.org/abs/2603.22263)|null|
|**2026-03-23**|**Closed-Loop Verbal Reinforcement Learning for Task-Level Robotic Planning**|Dmitrii Plotnikov et.al.|[2603.22169](http://arxiv.org/abs/2603.22169)|null|
|**2026-03-23**|**MEVIUS2: Practical Open-Source Quadruped Robot with Sheet Metal Welding and Multimodal Perception**|Kento Kawaharazuka et.al.|[2603.22031](http://arxiv.org/abs/2603.22031)|null|
|**2026-03-22**|**Dynasto: Validity-Aware Dynamic-Static Parameter Optimization for Autonomous Driving Testing**|Dmytro Humeniuk et.al.|[2603.21427](http://arxiv.org/abs/2603.21427)|null|
|**2026-03-22**|**Anatomical Prior-Driven Framework for Autonomous Robotic Cardiac Ultrasound Standard View Acquisition**|Zhiyan Cao et.al.|[2603.21134](http://arxiv.org/abs/2603.21134)|null|
|**2026-03-21**|**Speedup Patch: Learning a Plug-and-Play Policy to Accelerate Embodied Manipulation**|Zhichao Wu et.al.|[2603.20658](http://arxiv.org/abs/2603.20658)|null|
|**2026-03-20**|**AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning**|Huihua Zhao et.al.|[2603.20147](http://arxiv.org/abs/2603.20147)|null|
|**2026-03-20**|**Generalized Task-Driven Design of Soft Robots via Reduced-Order FEM-based Surrogate Modeling**|Yao Yao et.al.|[2603.19794](http://arxiv.org/abs/2603.19794)|null|
|**2026-03-19**|**Markov Potential Game and Multi-Agent Reinforcement Learning for Autonomous Driving**|Huiwen Yan et.al.|[2603.19188](http://arxiv.org/abs/2603.19188)|null|
|**2026-03-20**|**Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning**|Sangwoo Shin et.al.|[2603.19078](http://arxiv.org/abs/2603.19078)|null|
|**2026-03-19**|**Scaling Sim-to-Real Reinforcement Learning for Robot VLAs with Generative 3D Worlds**|Andrew Choi et.al.|[2603.18532](http://arxiv.org/abs/2603.18532)|null|
|**2026-03-18**|**DriveVLM-RL: Neuroscience-Inspired Reinforcement Learning with Vision-Language Models for Safe and Deployable Autonomous Driving**|Zilin Huang et.al.|[2603.18315](http://arxiv.org/abs/2603.18315)|null|
|**2026-03-18**|**EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards**|Ruixiang Wang et.al.|[2603.17808](http://arxiv.org/abs/2603.17808)|null|
|**2026-03-18**|**Interpreting Context-Aware Human Preferences for Multi-Objective Robot Navigation**|Tharun Sethuraman et.al.|[2603.17510](http://arxiv.org/abs/2603.17510)|null|
|**2026-03-18**|**Recurrent Reasoning with Vision-Language Models for Estimating Long-Horizon Embodied Task Progress**|Yuelin Zhang et.al.|[2603.17312](http://arxiv.org/abs/2603.17312)|null|
|**2026-03-18**|**WINFlowNets: Warm-up Integrated Networks Training of Generative Flow Networks for Robotics and Machine Fault Adaptation**|Zahin Sufiyan et.al.|[2603.17301](http://arxiv.org/abs/2603.17301)|null|
|**2026-03-17**|**Learning Whole-Body Control for a Salamander Robot**|Mengze Tian et.al.|[2603.16683](http://arxiv.org/abs/2603.16683)|null|
|**2026-03-17**|**When Should a Robot Think? Resource-Aware Reasoning via Reinforcement Learning for Embodied Robotic Decision-Making**|Jun Liu et.al.|[2603.16673](http://arxiv.org/abs/2603.16673)|null|
|**2026-03-17**|**Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models**|Yanru Wu et.al.|[2603.16065](http://arxiv.org/abs/2603.16065)|null|
|**2026-03-16**|**CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving**|Yihong Guo et.al.|[2603.15771](http://arxiv.org/abs/2603.15771)|null|
|**2026-03-16**|**From Passive Observer to Active Critic: Reinforcement Learning Elicits Process Reasoning for Robotic Manipulation**|Yibin Liu et.al.|[2603.15600](http://arxiv.org/abs/2603.15600)|null|
|**2026-03-16**|**KiRAS: Keyframe Guided Self-Imitation for Robust and Adaptive Skill Learning in Quadruped Robots**|Xiaoyi Wei et.al.|[2603.15179](http://arxiv.org/abs/2603.15179)|null|
|**2026-03-16**|**PerlAD: Towards Enhanced Closed-loop End-to-end Autonomous Driving with Pseudo-simulation-based Reinforcement Learning**|Yinfeng Gao et.al.|[2603.14908](http://arxiv.org/abs/2603.14908)|null|
|**2026-03-16**|**RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation**|Linfei Li et.al.|[2603.14880](http://arxiv.org/abs/2603.14880)|null|
|**2026-03-16**|**Ego to World: Collaborative Spatial Reasoning in Embodied Systems via Reinforcement Learning**|Heng Zhou et.al.|[2603.14811](http://arxiv.org/abs/2603.14811)|null|
|**2026-03-15**|**HomeGuard: VLM-based Embodied Safeguard for Identifying Contextual Risk in Household Task**|Xiaoya Lu et.al.|[2603.14367](http://arxiv.org/abs/2603.14367)|null|

## Imitation Learning & SFT

| Publish Date | Title | Authors | PDF | Code | 摘要 |
|:---------|:-----------------------|:---------|:------|:------|:-------------------------------------|
|**2026-08-27**|**Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation**|Wendong Li et.al.|[2608.27158](http://arxiv.org/abs/2608.27158)|null|<think> 好的，我现在需要帮用户总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，并且突出核心创新点，避免技术细节。用户还特别强调要直接输出总结内容，所有内容在同一行，不要换行符和其他解释。  首先，我得仔细阅读论文摘要，理解其核心内容。论文的问题是关于机器人群体导航中的短 hạn规划，现有强化学习方法输出单一反应动作，无法有效应对多样化的短时避让策略。方法部分提出了PDPO框架，结合离线预训练和在线微调，使用扩散策略生成五步行动块，并通过边界违反作为碰撞处理来避免无效行为。结论是PDPO在修改后的基准测试中表现优于基线，且行动块对结果至关重要。  接下来要确保符合格式要求，即问题、方法、结论三个部分，每个部分用方括号括起，用中文，并且总字数不超过300字。需要突出创新点，比如扩散策略生成行动块、边界违反作为碰撞处理，而不是详细的技术细节，比如具体的训练过程或实验设置。  还要注意用户可能没有明确提到的深层需求，比如他们可能需要这个总结用于快速了解论文核心，或者用于报告中的要点。因此，总结需要简洁、准确，同时涵盖问题、方法和结论的关键点。  现在开始组织语言。问题部分要简明指出当前方法的不足，方法部分强调PDPO的创新框架和关键改进，结论部分说明实验结果和关键发现。检查字数，确保不超过限制。同时确保没有使用换行符，所有内容在同一行。可能需要多次调整措辞，确保信息准确且符合格式要求。 </think> [问题]机器人群体导航中短 hạn规划需应对密集动态多模态人机交互，现有强化学习方法单步反应动作无法有效表征多样化避让策略[方法]提出PDPO框架，离线预训练扩散策略生成五步行动块，结合PPO在线微调，执行时递归应用，并将边界违反视为碰撞处理[结论]在修改边界基准测试中PDPO成功率高，验证行动块关键作用且边界约束机制有效|
|**2026-08-26**|**$R^3$ : Training Robots to Reason in Natural Language via Reinforcement Learning**|Lehong Wu et.al.|[2608.26053](http://arxiv.org/abs/2608.26053)|null|<think> 好的，我需要帮用户总结这篇论文，按照【问题】【方法】，总字数控制在300字以内，用中文。用户强调要突出核心创新点，避免技术细节，严格按照格式输出，所有内容在同一行，不换行，不加其他解释。  首先，仔细阅读论文摘要。问题部分是关于VLM能否通过自然语言推理提升机器人抓取能力，特别是在长任务中处理分解、约束跟踪、预测后果等挑战。方法部分提到了R³，分两步：先中期训练VLM用专家生成的推理痕迹初始化风格，再用基于评分的强化学习单步优化，使用离线动作数据。创新点在于使用非结构化语言推理，而不是结构化痕迹，作为测试时的指导。结论是R³在模拟任务中表现优于基线，说明自由语言推理可作为测试时计算机制。  接下来要精简问题和方法。问题要简明，方法突出创新点。注意不要技术细节，比如具体的训练步骤，但需要提到关键步骤和对比。结论部分要总结效果和意义。  检查字数，确保不超过300字。可能需要调整用词，比如“mid-trains”翻译为“中期训练”，“rubric-based RL”翻译为“评分强化学习”。确保格式正确，没有换行，用【】括起来，每部分之间用竖线分隔。  最后验证是否符合用户要求，核心创新点是自由形式语言推理，对比结构化痕迹，测试时指导动作。确保没有遗漏关键点，如模拟任务和对比结果。检查是否有技术细节，比如“Language Table”和“grocery packing”是否需要保留，但用户允许提到实例，所以保留。最终组合成一句话，符合格式。 </think> 【问题】VLM能否通过自然语言推理提升机器人长任务抓取能力，解决分解、约束跟踪等挑战；【方法】提出R³：中期训练VLM用专家推理痕迹初始化风格，结合评分强化学习单步优化离线动作数据，创新采用非结构化语言推理生成测试时动作指导；【结论】R³在模拟任务中优于指令模仿基线，验证自由语言推理可作为测试时计算机制优化探索与泛化。|
|**2026-08-26**|**VISTA: Visually Inferred Spatial ConTact Attention for Contact-Rich Manipulation**|Jiayi Chen et.al.|[2608.25872](http://arxiv.org/abs/2608.25872)|null|<think> 好的，我现在需要帮用户总结这篇论文，按照他们的格式要求。首先，用户给了一个具体的结构：问题、方法、结论，每部分要突出核心创新点，避免技术细节，控制在300字以内。  首先看论文标题和摘要。标题是VISTA: Visually Inferred Spatial ConTact Attention for Contact-Rich Manipulation。摘要里提到的问题是接触丰富的操作需要精确的交互反馈，但视觉方法在遮挡或轻微交互时有间接和模糊的线索，而专用触觉或力传感器会增加硬件复杂性和成本。所以问题部分应该总结为视觉反馈在接触检测中的不足，以及传统传感器的高成本。  接下来是方法部分。论文提出的方法是VISTA-Policy，利用视觉变形场（VDF）作为高维视觉-物理反馈。框架包括三个部分：物理感知编码引擎实时解码VDF，能量聚合去噪机制隔离真实信号，变形增强策略网络进行闭环修正。需要把这些核心点提炼出来，不用详细的技术细节。  结论部分要说明VISTA-Policy在多个任务中的表现优于纯视觉和触觉基线，尤其是一致性和成本效益，适合无结构环境。  用户强调要严格按照格式，所有内容在同一行，不要换行，不包含其他解释。所以需要检查字数是否在300以内，确保没有多余内容。可能需要注意术语的简化，比如“Energy Aggregation Denoising Mechanism”可以简化为“能量聚合去噪机制”，而“Deformation-Augmented Policy Network”可以简化为“变形增强策略网络”。  最后检查是否符合所有要求：核心创新点突出，结构正确，字数控制，没有换行。确认无误后输出。 </think> 问题：接触丰富操作依赖视觉反馈存在接触检测模糊且传感器成本高的问题；方法：提出VISTA-Policy通过视觉变形场（VDF）解码实时获取高维接触信息，结合能量聚合去噪和闭环修正策略提升精度；结论：在跨尺度抓取、开盖和书法等任务中优于纯视觉和触觉基线，具备强泛化性和低成本优势。|
|**2026-08-24**|**MomADv2: Reliable Temporal Memory for End-to-End Autonomous Driving**|Ziying Song et.al.|[2608.23405](http://arxiv.org/abs/2608.23405)|null|<think> 嗯，用户让我用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我需要仔细阅读论文摘要，抓住核心内容。  问题部分应该是关于长 hạn 规划中的记忆失效问题，当驾驶指令变化时，现有的记忆可能无效，导致错误决策。方法部分要突出选择性记忆查询模块和轨迹残差修正器，这两个是创新点。结论则是实验结果，碰撞率降低15.6%。  用户强调要突出核心创新点，避免技术细节。所以需要把问题、方法和结论分别用简洁的语言表达出来，不用深入解释模块的具体实现。同时，格式要求严格，同一行内，不换行，不要其他解释。  检查一下字数，确保不超过300字。可能需要调整用词，比如“长 hạn”换成“长时域”更准确。确认每个部分的关键词是否到位，比如“选择性状态空间规划记忆查询模块”和“流匹配轨迹残差修正器”是否准确。最后确保格式正确，没有换行，用【】括起来，各部分之间用竖线分隔。 </think> 【问题】长时域自动驾驶规划中驾驶指令变化导致历史记忆失效引发决策误导，需解决记忆筛选与指令一致性矛盾【方法】提出MomADv2框架，创新性设计选择性状态空间规划记忆查询模块动态过滤无效记忆，结合流匹配轨迹残差修正器通过连续残差场实现轨迹精细化修正【结论】在NAVSIM、Bench2Drive及nuScenes数据集验证，碰撞率较基线降低15.6%，显著提升长时域规划一致性。|
|**2026-08-24**|**Triplet2Track: A Hierarchical System with Object-Centric Representations for Reliable Long-Horizon Manipulation**|Jianxiang Liu et.al.|[2608.22800](http://arxiv.org/abs/2608.22800)|null|<think> 好的，我现在需要帮用户总结这篇论文，按照指定的格式来。首先，用户的要求很明确，要精简总结，控制在300字以内，严格按照【问题】【方法】，总字数不超过。用户还特别强调要突出核心创新点，避免技术细节，直接输出总结，不要换行符和其他解释。  首先，我得仔细阅读论文的摘要。问题部分主要是长 hạn（长周期）抓取在不确定环境中的可靠性问题，现有的方法要么数据量大且不透明（VLA模型），要么分层管道的可解释性高但计划与观察和低级动作对齐不够，缺乏在线反馈，导致开环行为和幻觉。方法部分，他们提出了Triplet-to-Track系统（TTS），使用人类视频减少数据依赖，将高层子目标表示为实例锚定的三元组，转化为连续轨迹先验执行，并通过观察监控任务进度进行在线重规划。结论是平均成功率74.8%，支持对象级和组合泛化。  接下来需要按照用户给的格式来组织。问题部分要简明扼要，方法部分突出创新点，比如人类视频、三元组表示、轨迹先验、在线监控。结论部分要包括成功率和泛化能力。要注意字数限制，必须严格控制每部分不超过规定字数，同时保持语句连贯，不使用技术细节。  然后检查是否符合所有要求：同一行内，无换行符，不包含其他解释。可能需要多次调整措辞，确保信息准确且简洁。例如，“长 hạn”翻译成中文是“长周期”，但用户给的标题是中文的，所以直接使用“长周期”。确认核心创新点是否突出，比如闭环系统、人类视频、三元组、在线重规划。避免提到具体数据如74.8%的成功率，但用户给的例子中有，可能需要保留。最后确保总字数在300以内，现在例子中的总结是符合的。  最后再通读一遍，确保没有遗漏关键点，格式正确，没有多余内容。确认无误后输出。 </think> 【问题】长周期抓取在不确定环境中可靠性差，现有方法数据依赖性强或分层管道计划与观察/低级动作对齐不足且缺乏在线反馈导致开环行为和幻觉【方法】提出闭环长周期模仿学习系统Triplet-to-Track，通过人类视频减少数据依赖，将高层子目标编码为实例|
|**2026-08-23**|**WorldToken: Time-First Sequence Modeling for Robotic Imitation Learning**|Chunkai Yang et.al.|[2608.22591](http://arxiv.org/abs/2608.22591)|null|<think> 好的，我现在需要处理用户的请求，帮他精简总结一篇论文。首先，用户的要求很明确：用中文，严格按照【问题】【方法】，总字数控制在300字以内，突出核心创新点，避免技术细节，直接输出总结内容，并且所有内容在同一行内，不能有换行符或其他解释。  首先，我得仔细阅读用户提供的论文信息。论文标题是“WorldToken: Time-First Sequence Modeling for Robotic Imitation Learning”，摘要里提到机器人策略在每一步决策时接收异构观察，而序列模型在如何组织这些输入的时间上存在差异。他们提出了WorldToken，这是一种时间优先的策略实例化方法，将多视角图像、本体感觉和任务条件在每一步策略时间步融合成一个世界令牌。然后使用因果时序Transformer建模这个令牌序列，扩散动作头生成动作片段。在23个RoboCasa任务中，一个85.3M参数的策略，结合预训练的CLIP文本编码器，达到了59.45%的平均闭环成功率，使用了2900个生成示范。实验部分测试了不同数据集大小、模型大小和训练种子，显示数据增加和模型尺寸增加带来收益，但历史可见性减少会降低成功率，比如在RMBench Blocks Ranking中可见历史从146秒减到8秒，成功率大幅下降。结论是验证了WorldToken的可行性，但未证明优于其他序列组织方式。  接下来，我需要按照用户指定的格式来总结。用户要求严格的问题和方法，结论部分可能不需要，但原问题部分可能需要更明确的问题描述。用户可能希望问题部分突出机器人模仿学习中的序列建模问题，而方法部分强调时间优先的融合和Transformer结构。需要注意避免技术细节，比如具体的参数数值、实验的具体设置等，但核心创新点如时间优先、融合多模态输入、因果Transformer和扩散动作头需要提到。  可能需要调整的问题描述是：机器人模仿学习中异构观测的时序建模问题导致策略性能受限。方法部分则是提出WorldToken，融合多模态输入为世界令牌，用因果Transformer建模，扩散头生成动作，并验证其有效性和数据/时间依赖性。  需要检查字数是否在300字以内，确保同一行，无换行符。同时要确保没有遗漏核心创新点，比如时间优先、多模态融合、因果Transformer、|
|**2026-08-21**|**WA-JEPA: Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving**|Xinlin Wang et.al.|[2608.20974](http://arxiv.org/abs/2608.20974)|null|<think> 好的，用户让我用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我需要仔细阅读论文摘要，找出核心问题和他们的解决方案。  论文标题提到WA-JEPA，是重新思考视频JEPA范式，针对自动驾驶中的世界-动作建模。问题部分应该说明现有V-JEPA的不足，比如随机掩码和确定性回归不适合自动驾驶规划，需要未来导向的预测结合动作。方法部分要突出他们的创新点：混合未来掩码预训练和条件流动匹配，还有联合预测器。结论部分则是性能提升和验证结果。  用户强调要突出核心创新点，避免技术细节。所以需要简化术语，比如“随机掩码完成”可以简化为“随机空间时间掩码”，但可能用户接受更简练的表达。注意字数限制，必须严格控制在300字以内，同时保持格式正确，同一行，无换行。  检查是否有遗漏的关键数据，比如EPDMS和HD-Score的提升，以及代码开源。这些在结论部分需要提到。要确保问题、方法、结论各部分清晰，没有冗余信息。最后确认是否符合格式要求，所有内容在同一行，没有其他解释。 </think> 问题：V-JEPA的随机空间时间掩码和确定性回归不适合自动驾驶未来导向的规划与动作预测；方法：提出WA-JEPA采用混合未来掩码预训练和条件流动匹配生成潜在未来，引入联合未来-动作预测器统一优化场景和轨迹；结论：在NAVSIM和HUGSIM上分别达到91.7 EPDMS和0.4462 HD-Score，超越基线且无需特定数据微调，验证V-JEPA原生世界动作建模范式有效性，代码开源。|
|**2026-08-21**|**Rethinking Demonstration Unlearning in Imitation Learning for Robotics**|Jiazhuo Li et.al.|[2608.20784](http://arxiv.org/abs/2608.20784)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，突出核心创新点，避免技术细节，直接输出总结，并且所有内容在同一行内，不要换行符。  首先，我得仔细阅读用户提供的论文摘要，理解问题和方法。论文的问题是关于机器人模仿学习中的示范重学（Demonstration Unlearning）的，现有的评估指标如遗忘损失或单成员攻击存在不足，无法有效评估编辑后的策略在闭环系统中的表现。因此，作者提出了新的评估框架，即retrain-calibrated audit，从行为轴和证据轴两个维度来评估。  接下来，我需要确定如何将问题和方法简洁地表达出来。问题部分要说明现有方法的不足，方法部分要突出两个新轴的引入以及结合验证。结论部分需要提到实验结果，比如两个轴的分离现象和实际应用效果。  然后，检查是否符合字数要求。用户要求300字以内，所以需要精炼语言，避免冗余。例如，问题部分可以简化为“机器人模仿学习依赖人类示范，但示范删除后重训成本高，现有评估指标无法验证编辑策略闭环性能”，方法部分则是“提出retrain-calibrated audit，从行为轴（对比重训策略动作分歧）和证据轴（单成员攻击检测残留证据）联合验证，结合独立重训构建基准线”。  还要注意用户强调的核心创新点，即两个轴的分离评估和联合验证，以及实验中的实际效果。需要确保这些点被突出，而技术细节如具体算法或实验条件可以省略。  最后，检查格式是否正确，确保没有换行符，所有内容在同一行内。可能需要多次调整措辞，确保信息准确且符合字数限制。例如，结论部分可以提到实验中两个轴的分离现象和成功案例，如ACT臂的编辑恢复机器人成功率。  现在，整合所有内容，确保每个部分简洁明了，符合用户的所有要求。可能还需要调整用词，比如将“retrain”翻译为“重训”更符合中文习惯，同时保持术语准确。最终形成符合要求的总结。 </think> 【问题】机器人模仿学习依赖人类示范，但示范删除后重训成本高，现有评估指标无法验证编辑策略闭环性能；【方法】提出retrain-calibrated|
|**2026-08-21**|**ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation**|Siyuan Ma et.al.|[2608.20735](http://arxiv.org/abs/2608.20735)|null|<think> 好的，用户让我用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我需要仔细阅读论文的标题和摘要，找出核心内容。  论文标题是“ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation”。摘要里提到的问题是，VLA政策通常基于当前观察，而世界行动模型（WAM）虽然能预测动态，但部署时成本高，比如视频规模教师或显式想象未来帧。方法部分，他们提出了ForeTime-VLA，使用一个冻结的Fast-WAM教师，生成未来行动的密集pi0.5政策，保持因果性。训练时加入多个目标，比如时间到过渡、相位等。结论部分，在测试集上MAE和L2有所下降，机器人评估中成功率和完成数优于基线。  用户要求突出核心创新点，避免技术细节。所以需要把问题简化为现有VLA政策依赖当前观察，WAM部署成本高。方法部分要强调未来令牌蒸馏和冻结教师，以及训练中的目标。结论则要提到性能提升和机器人评估结果。  要注意字数限制，必须严格控制在300字以内，并且所有内容在同一行，无换行。需要检查是否符合格式，是否有遗漏核心创新点，比如冻结教师、未来令牌、训练目标等。同时要确保语言简洁，不使用复杂术语，但准确传达信息。最后验证是否所有要求都满足，比如格式正确，没有多余解释，字数符合。 </think> 问题：Vision-Language-Action（VLA）政策依赖当前观察且世界行动模型（WAM）部署成本高；动态物体操作需预测接触事件但现有方法无法平衡预测精度与计算效率。方法：提出ForeTime-VLA，通过冻结Fast-WAM教师蒸馏未来行动令牌，构建64维未来目标，融合八帧历史编码预测时间-相位特征，用未来令牌约束视觉语言模型前缀并条件化动作专家，训练时结合多目标优化（时间-过渡、相位、几何关系等）。结论：在90次抓取任务中完成率提升50%（44/90 vs 23/90），快速带完成率提升400%（11/30 vs 2/30），机器人端静止/慢动抓取成功率分别达81.|
|**2026-08-20**|**RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement Learning in Robotic Manipulation**|Shaoxuan Wang et.al.|[2608.20208](http://arxiv.org/abs/2608.20208)|null|<think> 好的，我现在需要处理用户的请求，帮他精简总结一篇论文。首先，我得仔细阅读用户提供的资料，确保我完全理解他的要求。用户给了一个论文的标题、摘要，并指定了总结的格式：问题、方法、结论，每部分用方括号括起来，总字数控制在300字以内，还要突出核心创新点，避免技术细节，严格按照格式输出，且不要换行符或其他解释。  首先，我需要解析论文的问题。摘要中提到，现有的扩散和流匹配的机器人政策缺乏可计算的似然，限制了在基于似然的离线强化学习中的后训练应用。而AR-NFs虽然能提供表达式的动作建模和精确的似然评估，但存在序列采样带来的高开销，影响优化和部署。因此，问题应该是离线强化学习在机器人操作中应用AR-NFs时面临采样瓶颈，导致优化和部署效率低下。  接下来是方法部分。论文提出的RoMAN-Flow有两个核心创新：优化阶段采用无采样的优势加权似然目标，直接根据高优势动作分配高似然，避免采样；部署阶段将优化后的AR-NF政策蒸馏为单步生成器，降低推理延迟。这两个步骤解决了采样问题，提高了效率和实用性。  结论部分需要总结成果。实验表明，RoMAN-Flow在多个模拟和真实平台中达到竞争性政策性能，同时显著减少推理延迟，代码已开源。  现在需要检查是否符合用户的所有要求：格式正确，核心创新点突出，技术细节少，字数在限制内。要确保问题、方法、结论各部分简洁，用中文，没有换行符。可能需要注意术语的准确性，比如“AR-NFs”是否需要全称，但用户给的摘要中已经使用缩写，所以保持原样。最后确认字数，确保不超过300字，并且所有内容在同一行。 </think> [问题]离线强化学习在机器人操作中应用AR-NFs时存在采样瓶颈，导致优化和部署效率低下；[方法]RoMAN-Flow采用无采样优势加权似然优化和单步生成器部署，分别解决优化阶段采样开销和部署阶段推理延迟问题；[结论]实验验证其实现竞争性政策性能同时显著降低推理延迟，代码开源。|
|**2026-08-20**|**Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms**|Yanchen Guan et.al.|[2608.20111](http://arxiv.org/abs/2608.20111)|null|
|**2026-08-19**|**SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation**|Bowen Jing et.al.|[2608.18701](http://arxiv.org/abs/2608.18701)|null|
|**2026-08-19**|**HarvestPoint-ACT: Explicit Target Selection and Harvest-Point Conditioning for Robotic Fruit Harvesting under Occlusion**|Hanying Hu et.al.|[2608.18446](http://arxiv.org/abs/2608.18446)|null|
|**2026-08-18**|**Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics**|Shuangyu Xie et.al.|[2608.18227](http://arxiv.org/abs/2608.18227)|null|
|**2026-08-18**|**ORPA: Online Residual Policy Adaptation for Robot Manipulation Control with Human Feedback**|Muhammad A. Muttaqien et.al.|[2608.17323](http://arxiv.org/abs/2608.17323)|null|
|**2026-08-18**|**Robust Brachiation on a Life-Sized Dual-Arm Robot Using Waypoint-Guided Reinforcement Learning**|Ayumu Iwata et.al.|[2608.17320](http://arxiv.org/abs/2608.17320)|null|
|**2026-08-17**|**FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences**|Omar Rayyan et.al.|[2608.17027](http://arxiv.org/abs/2608.17027)|null|
|**2026-08-17**|**HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL**|Langzhe Gu et.al.|[2608.16837](http://arxiv.org/abs/2608.16837)|null|
|**2026-08-17**|**SurgVIL: Scaling Surgical Robot Imitation Learning with Open-source Surgical Videos**|Xinhao Chen et.al.|[2608.16058](http://arxiv.org/abs/2608.16058)|null|
|**2026-08-14**|**PILOT: Privileged Imitation Learning for End-to-End Motion Planning of Autonomous UAVs under Partial Observability**|Qingrui Zhang et.al.|[2608.14082](http://arxiv.org/abs/2608.14082)|null|
|**2026-08-13**|**FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving**|Zekai Li et.al.|[2608.12932](http://arxiv.org/abs/2608.12932)|null|
|**2026-08-06**|**$ω$ -0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation**|Zhe Li et.al.|[2608.06375](http://arxiv.org/abs/2608.06375)|null|
|**2026-08-06**|**VIDP: Variable Impedance Diffusion Policy for Compliant Robot Manipulation from Diverse Demonstrations**|Hisham Khalil et.al.|[2608.06210](http://arxiv.org/abs/2608.06210)|null|
|**2026-08-06**|**SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation**|Changyuan Wang et.al.|[2608.05970](http://arxiv.org/abs/2608.05970)|null|
|**2026-08-04**|**PFM-HR: Pose Flow Matching for Humanoid Robots**|Yukang Gao et.al.|[2608.03227](http://arxiv.org/abs/2608.03227)|null|
|**2026-08-02**|**WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autonomous Driving VLA**|Zhihao Zhu et.al.|[2608.01035](http://arxiv.org/abs/2608.01035)|null|
|**2026-08-02**|**RL Bootstrapping of OpenVLA-OFT for a Novel Robot Embodiment**|Damir Nurtdinov et.al.|[2608.01013](http://arxiv.org/abs/2608.01013)|null|
|**2026-08-01**|**Push-Wiper: Toward General-Purpose Robotic Cleaning across Varied Stains and Surfaces with Segmented Pushing Trajectories**|Renhao Lu et.al.|[2608.00730](http://arxiv.org/abs/2608.00730)|null|
|**2026-08-01**|**From Failures to Supervision: DynamicEnvPlan for Robust Long-Horizon Embodied Planning**|Hao Yuan et.al.|[2608.00613](http://arxiv.org/abs/2608.00613)|null|
|**2026-07-31**|**STAGE: STyle-controllable Action GEneration for personalized autonomous driving**|Zihao Liu et.al.|[2607.29517](http://arxiv.org/abs/2607.29517)|null|
|**2026-07-31**|**Temporal Policy: History-Initialized Action Generation for Robotic Learning from Demonstration**|Dylan Miller et.al.|[2607.29482](http://arxiv.org/abs/2607.29482)|null|
|**2026-07-31**|**BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning**|BWM Team et.al.|[2607.29302](http://arxiv.org/abs/2607.29302)|null|
|**2026-07-31**|**TRACT: Temporally Routed Action Chunks with Chronological Phase Authority for Contact-Rich Manipulation**|Jiahao Liu et.al.|[2607.29285](http://arxiv.org/abs/2607.29285)|null|
|**2026-07-31**|**CLIFT: Turning Gemini Robotics On-Device into Humanoid Specialists via Non-Invasive Closed-Loop Iterative Fine-Tuning**|Yuxin Chen et.al.|[2607.29172](http://arxiv.org/abs/2607.29172)|null|
|**2026-07-31**|**Outcome-Guided Distillation: A Teacher-Student Framework to Advance VLM Reasoning in Autonomous Driving**|Zeyu Dong et.al.|[2607.29052](http://arxiv.org/abs/2607.29052)|null|
|**2026-07-30**|**ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine**|Yukang Cao et.al.|[2607.28625](http://arxiv.org/abs/2607.28625)|null|
|**2026-07-30**|**FA-RDP: A Frequency-Adaptive Reactive Diffusion Policy for Contact-Rich Manipulation**|Lifeng Zhuo et.al.|[2607.28596](http://arxiv.org/abs/2607.28596)|null|
|**2026-07-29**|**Failure Detection for Surgical Robot Imitation Policies via Flow-Matching World Modeling**|Zhefeng Huang et.al.|[2607.27511](http://arxiv.org/abs/2607.27511)|null|
|**2026-07-28**|**MoMo: Dial Motion Mode in Robot Manipulation with Spatiotemporal Action Tokenization**|Yuhan Hu et.al.|[2607.26315](http://arxiv.org/abs/2607.26315)|null|
|**2026-07-28**|**S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information**|Kaneyoshi Hiratsuka et.al.|[2607.26047](http://arxiv.org/abs/2607.26047)|null|
|**2026-07-28**|**Tri-Manual Visuomotor Imitation Learning of Robot Policies**|James Zhao et.al.|[2607.25731](http://arxiv.org/abs/2607.25731)|null|
|**2026-07-23**|**GuidedAttention: Interpretable and Correctable Visual Attention for OOD-Robust Robot Manipulation via Imitation Learning**|Masaki Murooka et.al.|[2607.21049](http://arxiv.org/abs/2607.21049)|null|
|**2026-07-22**|**PerceptDrive: Perception Prior World-Action Modeling with Adaptive Expert Routing for End-to-End Autonomous Driving**|Yushan Liu et.al.|[2607.20175](http://arxiv.org/abs/2607.20175)|null|
|**2026-07-22**|**Diffusion ReRoll: Revisable Denoising for Robotic Sequential Prediction**|Seonsoo Kim et.al.|[2607.19919](http://arxiv.org/abs/2607.19919)|null|
|**2026-07-20**|**MEVION: Low-Cost Open-Source Data Collection System for Powerful and High-Speed Dual-Arm Manipulation**|Kento Kawaharazuka et.al.|[2607.17970](http://arxiv.org/abs/2607.17970)|null|
|**2026-07-17**|**Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation**|Zhenduo Shang et.al.|[2607.15880](http://arxiv.org/abs/2607.15880)|null|
|**2026-07-16**|**WorkDrive: Roadwork Chain of Causation for Autonomous Driving**|Tianyi Jiang et.al.|[2607.14727](http://arxiv.org/abs/2607.14727)|null|
|**2026-07-16**|**BridgeFlow: Fast and Robust SE(2)-Equivariant Motion Planning with Flow Matching**|Xinzhe Zhou et.al.|[2607.14725](http://arxiv.org/abs/2607.14725)|null|
|**2026-07-13**|**Mixture of Frames Policy: Multi-Frame Action Denoising for Bimanual Mobile Manipulation**|Dian Wang et.al.|[2607.11884](http://arxiv.org/abs/2607.11884)|null|
|**2026-07-13**|**Pix2Act: Image-Space Manipulation Policies with Equivariant Augmentation**|Haojie Huang et.al.|[2607.11167](http://arxiv.org/abs/2607.11167)|null|
|**2026-07-09**|**FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space**|Michael Murray et.al.|[2607.08877](http://arxiv.org/abs/2607.08877)|null|
|**2026-07-09**|**DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation**|Yunchao Yao et.al.|[2607.08751](http://arxiv.org/abs/2607.08751)|null|
|**2026-07-10**|**FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation**|Shiyuan Yang et.al.|[2607.08575](http://arxiv.org/abs/2607.08575)|null|
|**2026-07-08**|**Feedback Manipulation Regularization: Enabling Offline Agent Alignment for Imitation Learning**|Benjamin Poole et.al.|[2607.07859](http://arxiv.org/abs/2607.07859)|null|
|**2026-07-08**|**Shift & Drift: A Zero-Shot Benchmark for Generalizable and Robust Autonomous Driving Motion Planning**|Alessandro Canevaro et.al.|[2607.07844](http://arxiv.org/abs/2607.07844)|null|
|**2026-07-07**|**LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation**|Xinye Yang et.al.|[2607.06323](http://arxiv.org/abs/2607.06323)|null|
|**2026-07-06**|**Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation**|Jiaqi Peng et.al.|[2607.05377](http://arxiv.org/abs/2607.05377)|null|
|**2026-07-06**|**KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation**|Xinyu Shao et.al.|[2607.04652](http://arxiv.org/abs/2607.04652)|null|
|**2026-07-02**|**VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation**|Shuai Tian et.al.|[2607.02503](http://arxiv.org/abs/2607.02503)|null|
|**2026-07-02**|**EAGLE-360: Embodied Active Global-to-Local Exploration in 360 $^\circ$**|Jingtao Xu et.al.|[2607.02479](http://arxiv.org/abs/2607.02479)|null|
|**2026-07-02**|**WorldSample: Closed-loop Real-robot RL with World Modelling**|Yuquan Xue et.al.|[2607.02431](http://arxiv.org/abs/2607.02431)|null|
|**2026-07-02**|**One Demonstration Is Enough for Real-World Robotic Reinforcement Learning**|Yuwan Liu et.al.|[2607.01651](http://arxiv.org/abs/2607.01651)|null|
|**2026-06-30**|**ELMP: Efficient Learning for Motion Planning via Analytical Policy Gradients**|Yixiao Li et.al.|[2607.00215](http://arxiv.org/abs/2607.00215)|null|
|**2026-06-30**|**DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation**|Ziyu Shan et.al.|[2606.32028](http://arxiv.org/abs/2606.32028)|null|
|**2026-06-30**|**OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation**|Arnav Balaji et.al.|[2606.31993](http://arxiv.org/abs/2606.31993)|null|
|**2026-06-30**|**RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation**|Xinyi Wang et.al.|[2606.31836](http://arxiv.org/abs/2606.31836)|null|
|**2026-06-30**|**Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot**|Ethan Marot et.al.|[2606.31807](http://arxiv.org/abs/2606.31807)|null|
|**2026-06-29**|**OpenSPM: An Environment-Transferable Robotic Key Spatial Pose Memory and Closed-Loop High-Frequency Flow-Matching Action Generation Model**|Iok Tong Lei et.al.|[2606.29936](http://arxiv.org/abs/2606.29936)|null|
|**2026-06-28**|**CORE: Common Outcome Regularities from Action-Free Visual Demonstrations for Robot Manipulation**|Juyi Sheng et.al.|[2606.29517](http://arxiv.org/abs/2606.29517)|null|
|**2026-06-26**|**LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior**|Qinhong Zhou et.al.|[2606.28182](http://arxiv.org/abs/2606.28182)|null|
|**2026-06-25**|**Bridging Handheld and Teleoperated Supervision for Contact-Rich Manipulation via State-Gated Experts**|Vidullan Surendran et.al.|[2606.26603](http://arxiv.org/abs/2606.26603)|null|
|**2026-06-24**|**Learning Action Priors for Cross-embodiment Robot Manipulation**|Dong Jing et.al.|[2606.26095](http://arxiv.org/abs/2606.26095)|null|
|**2026-06-24**|**Stage-Aware and Roughness-Constrained Diffusion Policy for Multi-Stage Robotic Polishing**|Shuai Ke et.al.|[2606.25754](http://arxiv.org/abs/2606.25754)|null|
|**2026-06-24**|**One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand**|Piotr Koczy et.al.|[2606.25575](http://arxiv.org/abs/2606.25575)|null|
|**2026-06-24**|**ASSCG: Just-Right Gating over Chattering for Fast-Slow LLM Planning in Autonomous Driving**|Sining Ang et.al.|[2606.25509](http://arxiv.org/abs/2606.25509)|null|
|**2026-06-23**|**Beyond Monotonic Progress: Retry-Supervised Value Learning for Robot Imitation**|Xinyao Qin et.al.|[2606.24633](http://arxiv.org/abs/2606.24633)|null|
|**2026-06-23**|**RE4: Transformation-aware Imitation of Object Interactions Using Manipulation Modes**|Arsh Chawla et.al.|[2606.24403](http://arxiv.org/abs/2606.24403)|null|
|**2026-06-21**|**ARP: Enhancing Quantized Skill Abstractions via Visual Alignment and Iterative Refinement for Robotic Manipulation**|Yuntian Wang et.al.|[2606.22480](http://arxiv.org/abs/2606.22480)|null|
|**2026-06-21**|**Do Rigid-Body Simulators Dream of Soft Robots? Learning Contact-Rich Manipulation for Tendon-Driven Continuum Robots**|Chengnan Shentu et.al.|[2606.22397](http://arxiv.org/abs/2606.22397)|null|
|**2026-06-21**|**FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation**|Kexin Shi et.al.|[2606.22303](http://arxiv.org/abs/2606.22303)|null|
|**2026-06-20**|**CoRDE: Concept-Prior Routed Diffusion Experts for Structural Generalization in Robot Manipulation**|Haidong Huang et.al.|[2606.21935](http://arxiv.org/abs/2606.21935)|null|
|**2026-06-18**|**CoLI: A Reproducible Platform for Continuum Robot Learning via Monolithic 3D Printing and Isomorphic Teleoperation**|Ziyuan Tang et.al.|[2606.20389](http://arxiv.org/abs/2606.20389)|null|
|**2026-06-18**|**Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation**|Jianing Guo et.al.|[2606.20135](http://arxiv.org/abs/2606.20135)|null|
|**2026-06-18**|**Co-policy: Responsive Human-Robot Co-Creation for Musical Performances**|Xuetao Li et.al.|[2606.19914](http://arxiv.org/abs/2606.19914)|null|
|**2026-06-17**|**Invertible Neural Network Adapter for One-Step Flow Matching in Robot Manipulation**|Yu Zhang et.al.|[2606.19194](http://arxiv.org/abs/2606.19194)|null|
|**2026-06-16**|**WireCraft: A Simulation Benchmark for Industrial DLO Manipulation**|Chongyu Zhu et.al.|[2606.18097](http://arxiv.org/abs/2606.18097)|null|
|**2026-06-16**|**LAGO Policy: Latency-Aware Asynchronous Diffusion Policies with Goal-Directed Collision-Free Planning for Smooth Manipulation**|Guowei Shi et.al.|[2606.17982](http://arxiv.org/abs/2606.17982)|null|
|**2026-06-16**|**When Robots Sleep: Offline Skill Consolidation for Shared-Policy Robot Learning**|Nethmi Jayasinghe et.al.|[2606.17493](http://arxiv.org/abs/2606.17493)|null|
|**2026-06-15**|**Steering Generative Reinforcement Learning into Stable Robotic Controller**|Yixuan Wang et.al.|[2606.16572](http://arxiv.org/abs/2606.16572)|null|
|**2026-06-15**|**APEX: Adaptive Policy Execution for Precise Manipulation**|Mengfei Zhao et.al.|[2606.16504](http://arxiv.org/abs/2606.16504)|null|
|**2026-06-12**|**Spatially Conditioned Diffusion Policy: Learning Precise and Robust Manipulation with a Single RGB Camera**|Seoyoon Kim et.al.|[2606.14535](http://arxiv.org/abs/2606.14535)|null|
|**2026-06-12**|**Kine2Go: Kinematic dataset for the Unitree Go2 robot with diverse gaits and motions**|Władysław Pałucki et.al.|[2606.14433](http://arxiv.org/abs/2606.14433)|null|
|**2026-06-12**|**Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack**|He Zhang et.al.|[2606.14409](http://arxiv.org/abs/2606.14409)|null|
|**2026-06-12**|**Improving Robotic Generalist Policies via Flow Reversal Steering**|Andy Tang et.al.|[2606.13675](http://arxiv.org/abs/2606.13675)|null|
|**2026-06-11**|**$\texttt{WEAVER}$ , Better, Faster, Longer: An Effective World Model for Robotic Manipulation**|Arnav Kumar Jain et.al.|[2606.13672](http://arxiv.org/abs/2606.13672)|null|
|**2026-06-11**|**AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots**|Jianli Sun et.al.|[2606.12859](http://arxiv.org/abs/2606.12859)|null|
|**2026-06-10**|**Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics**|Adam Wei et.al.|[2606.12365](http://arxiv.org/abs/2606.12365)|null|
|**2026-06-10**|**DuoBench: A Reproducible Benchmark for Bimanual Manipulation in Simulation and the Real World**|Tobias Jülg et.al.|[2606.11901](http://arxiv.org/abs/2606.11901)|null|
|**2026-06-10**|**Critic Architecture Matters: Dual vs. Unified Critics for Humanoid Loco-Manipulation**|Mehmet Turan Yardımcı et.al.|[2606.11891](http://arxiv.org/abs/2606.11891)|null|
|**2026-06-09**|**TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation**|Yujie Zang et.al.|[2606.11184](http://arxiv.org/abs/2606.11184)|null|
|**2026-06-09**|**IMPACT: Learning Internal-Model Predictive Control for Forceful Robotic Manipulation**|Jiawei Gao et.al.|[2606.10818](http://arxiv.org/abs/2606.10818)|null|
|**2026-06-09**|**Test-time Adversarial Takeover: A Real-time Hijacking Interface against Robotic Diffusion Policies**|Zi Yin et.al.|[2606.10371](http://arxiv.org/abs/2606.10371)|null|
|**2026-06-05**|**Spline Policy: A Structured Representation for Robot Policies**|Mengze Tian et.al.|[2606.07386](http://arxiv.org/abs/2606.07386)|null|
|**2026-06-05**|**ActionMap: Robot Policy Learning via Voxel Action Heatmap**|Pei Yang et.al.|[2606.06904](http://arxiv.org/abs/2606.06904)|null|
|**2026-06-04**|**Multi-Resolution Tactile Imitation Learning for Contact-Rich Robotic Manipulation**|Rickmer Krohn et.al.|[2606.06281](http://arxiv.org/abs/2606.06281)|null|
|**2026-06-04**|**L-SDPPO: Policy Optimization of Spiking Diffusion Policy for Intra-vehicular Robotic Manipulation**|Liwen Zhang et.al.|[2606.06049](http://arxiv.org/abs/2606.06049)|null|
|**2026-06-04**|**Towards a Data Flywheel for Embodied Intelligence in Logistics**|Anlan Yu et.al.|[2606.05960](http://arxiv.org/abs/2606.05960)|null|
|**2026-06-01**|**Co-training with Ego-centric Video and Demonstration for Robot Navigation Task**|Shoya Kuno et.al.|[2606.01951](http://arxiv.org/abs/2606.01951)|null|
|**2026-05-31**|**Expanding Spatial and Temporal Context for Robotic Imitation Learning With Scene Graphs**|Jianing Qian et.al.|[2606.01072](http://arxiv.org/abs/2606.01072)|null|
|**2026-05-30**|**DriveAnchor: Progressive Anchor-based Flow Learning for Autonomous Driving Planning**|Limin Yan et.al.|[2606.00519](http://arxiv.org/abs/2606.00519)|null|
|**2026-05-29**|**Surface Constraint Policy for Learning Surface-Constrained and Dynamically Feasible Robot Skills**|Shuai Ke et.al.|[2605.31321](http://arxiv.org/abs/2605.31321)|null|
|**2026-05-29**|**DeMaVLA: A Vision-Language-Action Foundation Model for Generalizable Deformable Manipulation**|Taiyi Su et.al.|[2605.31286](http://arxiv.org/abs/2605.31286)|null|
|**2026-05-27**|**Imitation Learning for Robot Assistance in Open Surgery: A Multi-Policy Evaluation on Suture Following**|Xucheng Wang et.al.|[2605.28736](http://arxiv.org/abs/2605.28736)|null|
|**2026-05-27**|**DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving**|Chen Shi et.al.|[2605.28544](http://arxiv.org/abs/2605.28544)|null|
|**2026-05-27**|**ProgVLA: Progress-Aware Robot Manipulation Skill Learning**|Seungsu Kim et.al.|[2605.28231](http://arxiv.org/abs/2605.28231)|null|
|**2026-05-26**|**TPS-Drive: Task-Guided Representation Purification for VLM-based Autonomous Driving**|Jiaxiang Li et.al.|[2605.27038](http://arxiv.org/abs/2605.27038)|null|
|**2026-05-22**|**Semantically Structured Mixture-of-Experts for Compositional Robotic Manipulation**|Chengyu Deng et.al.|[2605.23477](http://arxiv.org/abs/2605.23477)|null|
|**2026-05-21**|**Factored Diffusion Policies:Compositionally Generalized Robot Control with a Single Score Network**|Sayan Mitra et.al.|[2605.22596](http://arxiv.org/abs/2605.22596)|null|
|**2026-05-20**|**Distill to Think, Foresee to Act: Cognitive-Physical Reinforcement Learning for Autonomous Driving**|Yang Wu et.al.|[2605.21139](http://arxiv.org/abs/2605.21139)|null|
|**2026-05-20**|**Mobile UMI: Cross-View Diffusion Policy with Decoupled Kinematics for Mobile Manipulation**|Haoran Huang et.al.|[2605.20894](http://arxiv.org/abs/2605.20894)|null|
|**2026-05-19**|**Beyond Action Residuals: Real-World Robot Policy Steering via Bottleneck Latent Reinforcement Learning**|Dongjie Yu et.al.|[2605.19919](http://arxiv.org/abs/2605.19919)|null|
|**2026-05-19**|**Beyond Imitation: Learning Safe End-to-End Autonomous Driving from Hard Negatives**|Junli Wang et.al.|[2605.19771](http://arxiv.org/abs/2605.19771)|null|
|**2026-05-19**|**SafeAlign-VLA: A Negative-Enhanced Safe Alignment Framework for Risk-Aware Autonomous Driving**|Kefei Tian et.al.|[2605.19524](http://arxiv.org/abs/2605.19524)|null|
|**2026-05-19**|**Neuromorphic Control of a Flapping-Wing Robot on Resource-Constrained Hardware**|Rim El Filali et.al.|[2605.19430](http://arxiv.org/abs/2605.19430)|null|
|**2026-05-17**|**HCLM: A Hierarchical Framework for Cooperative Loco-Manipulation with Dual Quadrupeds**|Qixuan Li et.al.|[2605.17300](http://arxiv.org/abs/2605.17300)|null|
|**2026-05-16**|**SADP: Subgoal-Aware Diffusion Policy for Explainable Robots Learned from Foundation Model Generated Demonstrations**|Site Hu et.al.|[2605.16871](http://arxiv.org/abs/2605.16871)|null|
|**2026-05-14**|**Learning Direct Control Policies with Flow Matching for Autonomous Driving**|Marcello Ceresini et.al.|[2605.14832](http://arxiv.org/abs/2605.14832)|null|
|**2026-05-13**|**MAPLE: Latent Multi-Agent Play for End-to-End Autonomous Driving**|Rajeev Yasarla et.al.|[2605.14201](http://arxiv.org/abs/2605.14201)|null|
|**2026-05-13**|**SID: Sliding into Distribution for Robust Few-Demonstration Manipulation**|Yicheng Ma et.al.|[2605.13428](http://arxiv.org/abs/2605.13428)|null|
|**2026-05-12**|**Morphologically Equivariant Flow Matching for Bimanual Mobile Manipulation**|Max Siebenborn et.al.|[2605.12228](http://arxiv.org/abs/2605.12228)|null|
|**2026-05-11**|**HeteroGenManip: Generalizable Manipulation For Heterogeneous Object Interactions**|Zhenhao Shen et.al.|[2605.10201](http://arxiv.org/abs/2605.10201)|null|
|**2026-05-11**|**Data-Asymmetric Latent Imagination and Reranking for 3D Robotic Imitation Learning**|Lianghao Luo et.al.|[2605.10166](http://arxiv.org/abs/2605.10166)|null|
|**2026-05-11**|**StereoPolicy: Improving Robotic Manipulation Policies via Stereo Perception**|Evans Han et.al.|[2605.09989](http://arxiv.org/abs/2605.09989)|null|
|**2026-05-07**|**OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation**|Yushan Liu et.al.|[2605.06481](http://arxiv.org/abs/2605.06481)|null|
|**2026-05-01**|**MSACT: Multistage Spatial Alignment for Stable Low-Latency Fine Manipulation**|Xianbo Cai et.al.|[2605.00475](http://arxiv.org/abs/2605.00475)|null|
|**2026-05-01**|**Stereo Multistage Spatial Attention for Real-Time Mobile Manipulation Under Visual Scale Variation and Disturbances**|Xianbo Cai et.al.|[2605.00471](http://arxiv.org/abs/2605.00471)|null|
|**2026-05-01**|**Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies**|Yi Wang et.al.|[2605.00416](http://arxiv.org/abs/2605.00416)|null|
|**2026-04-28**|**KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning**|Yixuan Huang et.al.|[2604.25788](http://arxiv.org/abs/2604.25788)|null|
|**2026-04-26**|**Tube Diffusion Policy: Reactive Visual-Tactile Policy Learning for Contact-rich Manipulation**|Teng Xue et.al.|[2604.23609](http://arxiv.org/abs/2604.23609)|null|
|**2026-04-23**|**FingerEye: Continuous and Unified Vision-Tactile Sensing for Dexterous Manipulation**|Zhixuan Xu et.al.|[2604.20689](http://arxiv.org/abs/2604.20689)|null|
|**2026-04-22**|**Stability-Driven Motion Generation for Object-Guided Human-Human Co-Manipulation**|Jiahao Xu et.al.|[2604.20336](http://arxiv.org/abs/2604.20336)|null|
|**2026-04-15**|**HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System**|Tianshuo Yang et.al.|[2604.14125](http://arxiv.org/abs/2604.14125)|null|
|**2026-04-14**|**Whole-Body Mobile Manipulation using Offline Reinforcement Learning on Sub-optimal Controllers**|Snehal Jauhri et.al.|[2604.12509](http://arxiv.org/abs/2604.12509)|null|
|**2026-04-13**|**AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation**|Mingyang Li et.al.|[2604.11674](http://arxiv.org/abs/2604.11674)|null|
|**2026-04-12**|**LIDEA: Human-to-Robot Imitation Learning via Implicit Feature Distillation and Explicit Geometry Alignment**|Yifu Xu et.al.|[2604.10677](http://arxiv.org/abs/2604.10677)|null|
|**2026-04-12**|**OmniUMI: Towards Physically Grounded Robot Learning via Human-Aligned Multimodal Interaction**|Shaqi Luo et.al.|[2604.10647](http://arxiv.org/abs/2604.10647)|null|
|**2026-04-12**|**AffordGen: Generating Diverse Demonstrations for Generalizable Object Manipulation with Afford Correspondence**|Jiawei Zhang et.al.|[2604.10579](http://arxiv.org/abs/2604.10579)|null|
|**2026-04-11**|**MoRI: Mixture of RL and IL Experts for Long-Horizon Manipulation Tasks**|Yaohang Xu et.al.|[2604.10165](http://arxiv.org/abs/2604.10165)|null|
|**2026-04-10**|**VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis**|Xiaolei Lang et.al.|[2604.09330](http://arxiv.org/abs/2604.09330)|null|
|**2026-04-10**|**Learning Vision-Language-Action World Models for Autonomous Driving**|Guoqing Wang et.al.|[2604.09059](http://arxiv.org/abs/2604.09059)|null|
|**2026-04-09**|**Generative Simulation for Policy Learning in Physical Human-Robot Interaction**|Junxiang Wang et.al.|[2604.08664](http://arxiv.org/abs/2604.08664)|null|
|**2026-04-09**|**LAMP: Lift Image-Editing as General 3D Priors for Open-world Manipulation**|Jingjing Wang et.al.|[2604.08475](http://arxiv.org/abs/2604.08475)|null|
|**2026-04-09**|**HiRO-Nav: Hybrid ReasOning Enables Efficient Embodied Navigation**|He Zhao et.al.|[2604.08232](http://arxiv.org/abs/2604.08232)|null|
|**2026-04-09**|**HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation**|Shuanghao Bai et.al.|[2604.07993](http://arxiv.org/abs/2604.07993)|null|
|**2026-04-08**|**Flow Motion Policy: Manipulator Motion Planning with Flow Matching Models**|Davood Soleymanzadeh et.al.|[2604.07084](http://arxiv.org/abs/2604.07084)|null|
|**2026-04-08**|**RichMap: A Reachability Map Balancing Precision, Efficiency, and Flexibility for Rich Robot Manipulation Tasks**|Yupu Lu et.al.|[2604.06778](http://arxiv.org/abs/2604.06778)|null|
|**2026-04-04**|**Build on Priors: Vision--Language--Guided Neuro-Symbolic Imitation Learning for Data-Efficient Real-World Robot Manipulation**|Pierrick Lorang et.al.|[2604.03759](http://arxiv.org/abs/2604.03759)|null|
|**2026-04-04**|**Human-Robot Copilot for Data-Efficient Imitation Learning**|Rui Yan et.al.|[2604.03613](http://arxiv.org/abs/2604.03613)|null|
|**2026-04-09**|**Drift-Based Policy Optimization: Native One-Step Policy Learning for Online Robot Control**|Yuxuan Gao et.al.|[2604.03540](http://arxiv.org/abs/2604.03540)|null|
|**2026-04-04**|**Optimizing Neurorobot Policy under Limited Demonstration Data through Preference Regret**|Viet Dung Nguyen et.al.|[2604.03523](http://arxiv.org/abs/2604.03523)|null|
|**2026-04-03**|**A Flow Matching Framework for Soft-Robot Inverse Dynamics**|Hang Yang et.al.|[2604.03006](http://arxiv.org/abs/2604.03006)|null|
|**2026-04-03**|**OMNI-PoseX: A Fast Vision Model for 6D Object Pose Estimation in Embodied Tasks**|Michael Zhang et.al.|[2604.02759](http://arxiv.org/abs/2604.02759)|null|
|**2026-04-03**|**ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving**|Zihao Sheng et.al.|[2604.02714](http://arxiv.org/abs/2604.02714)|null|
|**2026-04-02**|**UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models**|Qiyao Zhang et.al.|[2604.02241](http://arxiv.org/abs/2604.02241)|null|
|**2026-04-02**|**AnchorVLA: Anchored Diffusion for Efficient End-to-End Mobile Manipulation**|Jia Syuen Lim et.al.|[2604.01567](http://arxiv.org/abs/2604.01567)|null|
|**2026-04-01**|**Multi-Camera View Scaling for Data-Efficient Robot Imitation Learning**|Yichen Xie et.al.|[2604.00557](http://arxiv.org/abs/2604.00557)|null|
|**2026-03-31**|**Generalizable Dense Reward for Long-Horizon Robotic Tasks**|Silong Yong et.al.|[2604.00055](http://arxiv.org/abs/2604.00055)|null|
|**2026-03-31**|**HapCompass: A Rotational Haptic Device for Contact-Rich Robotic Teleoperation**|Xiangshan Tan et.al.|[2603.30042](http://arxiv.org/abs/2603.30042)|null|
|**2026-03-31**|**PRISM: A Multi-View Multi-Capability Retail Video Dataset for Embodied Vision-Language Models**|Amirreza Rouhi et.al.|[2603.29281](http://arxiv.org/abs/2603.29281)|null|
|**2026-03-30**|**SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning**|Philip Schroeder et.al.|[2603.28730](http://arxiv.org/abs/2603.28730)|null|
|**2026-03-30**|**Active Stereo-Camera Outperforms Multi-Sensor Setup in ACT Imitation Learning for Humanoid Manipulation**|Robin Kühn et.al.|[2603.28422](http://arxiv.org/abs/2603.28422)|null|
|**2026-03-29**|**ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation**|Hongyu Yan et.al.|[2603.27670](http://arxiv.org/abs/2603.27670)|null|
|**2026-03-27**|**UMI-Underwater: Learning Underwater Manipulation without Underwater Teleoperation**|Hao Li et.al.|[2603.27012](http://arxiv.org/abs/2603.27012)|null|
|**2026-03-31**|**DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching**|Jiayi Chen et.al.|[2603.26320](http://arxiv.org/abs/2603.26320)|null|
|**2026-03-26**|**Towards Embodied AI with MuscleMimic: Unlocking full-body musculoskeletal motor learning at scale**|Chengkun Li et.al.|[2603.25544](http://arxiv.org/abs/2603.25544)|null|
|**2026-03-26**|**$π$ , But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation**|Johnathan Tucker et.al.|[2603.25038](http://arxiv.org/abs/2603.25038)|null|
|**2026-03-25**|**FODMP: Fast One-Step Diffusion of Movement Primitives Generation for Time-Dependent Robot Actions**|Xirui Shi et.al.|[2603.24806](http://arxiv.org/abs/2603.24806)|null|
|**2026-03-24**|**Efficient Hybrid SE(3)-Equivariant Visuomotor Flow Policy via Spherical Harmonics for Robot Manipulation**|Qinglun Zhang et.al.|[2603.23227](http://arxiv.org/abs/2603.23227)|null|
|**2026-03-24**|**DecompGrind: A Decomposition Framework for Robotic Grinding via Cutting-Surface Planning and Contact-Force Adaptation**|Shunsuke Araki et.al.|[2603.22859](http://arxiv.org/abs/2603.22859)|null|
|**2026-03-24**|**SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation**|Ruisen Tu et.al.|[2603.22760](http://arxiv.org/abs/2603.22760)|null|
|**2026-03-19**|**From Inference Efficiency to Embodied Efficiency: Revisiting Efficiency Metrics for Vision-Language-Action Models**|Zhuofan Li et.al.|[2603.19131](http://arxiv.org/abs/2603.19131)|null|
|**2026-03-19**|**V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors**|Songjia He et.al.|[2603.18811](http://arxiv.org/abs/2603.18811)|null|
|**2026-03-18**|**Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control**|Zunzhe Zhang et.al.|[2603.17834](http://arxiv.org/abs/2603.17834)|null|
|**2026-03-18**|**VolumeDP: Modeling Volumetric Representation for Manipulation Policy Learning**|Tianxing Zhou et.al.|[2603.17720](http://arxiv.org/abs/2603.17720)|null|
|**2026-03-17**|**MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation**|Abhay Deshpande et.al.|[2603.16861](http://arxiv.org/abs/2603.16861)|null|
|**2026-03-17**|**Conservative Offline Robot Policy Learning via Posterior-Transition Reweighting**|Wanpeng Zhang et.al.|[2603.16542](http://arxiv.org/abs/2603.16542)|null|
|**2026-03-17**|**Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation**|Chang Nie et.al.|[2603.16086](http://arxiv.org/abs/2603.16086)|null|
|**2026-03-22**|**Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models**|Yanru Wu et.al.|[2603.16065](http://arxiv.org/abs/2603.16065)|null|
|**2026-03-16**|**CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving**|Yihong Guo et.al.|[2603.15771](http://arxiv.org/abs/2603.15771)|null|
|**2026-03-16**|**You've Got a Golden Ticket: Improving Generative Robot Policies With A Single Noise Vector**|Omkar Patil et.al.|[2603.15757](http://arxiv.org/abs/2603.15757)|null|
|**2026-03-16**|**From Passive Observer to Active Critic: Reinforcement Learning Elicits Process Reasoning for Robotic Manipulation**|Yibin Liu et.al.|[2603.15600](http://arxiv.org/abs/2603.15600)|null|
|**2026-03-16**|**MoE-ACT: Scaling Multi-Task Bimanual Manipulation with Sparse Language-Conditioned Mixture-of-Experts Transformers**|Kangjun Guo et.al.|[2603.15265](http://arxiv.org/abs/2603.15265)|null|
|**2026-03-16**|**HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing**|Konstantin Gubernatorov et.al.|[2603.15257](http://arxiv.org/abs/2603.15257)|null|
|**2026-03-16**|**KiRAS: Keyframe Guided Self-Imitation for Robust and Adaptive Skill Learning in Quadruped Robots**|Xiaoyi Wei et.al.|[2603.15179](http://arxiv.org/abs/2603.15179)|null|

[contributors-shield]: https://img.shields.io/github/contributors/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/HuJiaming11/rl-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/HuJiaming11/rl-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/HuJiaming11/rl-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/HuJiaming11/rl-arxiv-daily/issues

