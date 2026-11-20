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

## Updated on 2026.11.20
> Usage instructions: [here](./docs/README.md#usage)

## Reinforcement Learning

| Publish Date | Title | Authors | PDF | Code | 摘要 |
|:---------|:-----------------------|:---------|:------|:------|:-------------------------------------|
|**2026-11-19**|**Exposure-Aware Informative Path Planning Using Deep Reinforcement Learning**|Muzaffar Qureshi et.al.|[2611.26302](http://arxiv.org/abs/2611.26302)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照【问题】【方法】，总字数控制在300字以内。用户还特别强调要突出核心创新点，避免技术细节，并且严格按照指定格式输出，不要换行符和其他解释。  首先，我得仔细阅读论文的摘要。问题部分提到的是在有限预算下，车队移动传感器的信息路径规划（IPP）问题，同时要限制高场强度区域的暴露。现有方法优化信息量时没有考虑场暴露约束。方法部分是提出了一个参数共享的PPO框架，结合了分布式演员和集中式批评家，训练后评估。结论显示在多个场景下，EA-IPP在保持信息量的同时降低了暴露。  接下来要提炼核心创新点。问题核心是有限预算下的信息路径规划，同时考虑场暴露。方法上的创新在于将场暴露约束转化为双目标优化，使用共享PPO框架。结论部分要突出在三个场景下的性能提升，尤其是信息增益和暴露降低的数据。  需要注意避免技术细节，比如具体的算法名称（如PPO）可能需要简化，但用户给的例子中保留了PPO，所以可能需要保留。同时要确保每个部分简洁，问题、方法、结论各部分用竖线分隔，总字数控制在300字内。  检查用户给的例子，他们用了“提出参数共享PPO框架”这样的表达，所以可能需要类似的结构。确保每个部分不超过两句话，信息准确，不遗漏关键数据，如三个场景的暴露降低百分比。  最后，确保格式正确，所有内容在同一行，没有换行符，严格按照【问题】【方法】，总字数符合要求。可能需要多次调整措辞，确保精简同时包含所有必要信息。 </think> 【问题】有限预算下移动传感车队在未知标量场的信息路径规划需同时限制高场强度区域暴露，现有方法未融合场暴露约束；【方法】提出参数共享PPO框架将场暴露约束转化为双目标优化，结合分布式演员与集中式批评家进行离线训练；【结论】在雷达/烟雾/野火场景中，该框架在保持信息增益接近最优水平的同时，使场暴露分别降低34.6%/20.1%/27%，信息重构RMSE最优。|
|**2026-11-19**|**EmbodyAgent: Post-Training Embodied VLM Agents via Distillation, SFT, and RL**|Wei Dai et.al.|[2611.26196](http://arxiv.org/abs/2611.26196)|null|<think> 好的，我现在需要帮用户总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，用中文精简总结，突出核心创新点，避免技术细节，直接输出格式。  先看论文标题和摘要。标题是EmbodyAgent，关于通过蒸馏、SFT和RL进行后训练的具身化VLM代理。摘要里提到的问题有三个：开放权重VLM转化为高性能具身代理需要完整后训练栈，但现有方法存在工具接口交互失败、教师模型不可访问权重、监督模仿 plateau 的问题。  接下来是方法部分。论文提出了三个紧密耦合的流程：黑盒数据合成、SFT蒸馏、在线RL优化。核心创新点应该是这三个流程的整合，特别是使用黑盒教师生成轨迹，蒸馏成可训练的VLM，以及RL优化时处理代码执行错误。结论部分提到在评估中成功率从0到84，训练成功率87.7%，模型调用减少，还有错误模式分析和监控机制。  用户要求避免技术细节，所以需要提炼每个部分的关键点。问题部分要简明指出三个主要挑战。方法部分强调三个流程的协同，特别是黑盒数据合成、SFT蒸馏和RL优化中的奖励设计。结论部分突出性能提升和错误处理机制。  需要注意格式，所有内容在同一行，用【问题】【方法】，总字数不超过300字。要检查是否有换行符，确保符合用户格式要求。可能用户是研究人员或学生，需要快速了解论文核心，所以总结要准确且重点突出，不涉及具体实验数据细节，但关键成果如成功率提升和模型调用减少要包含进去。  最后检查是否符合要求，确保没有多余的解释，严格按照格式输出。可能需要注意术语的准确性，比如“SFT”要展开为“监督微调（SFT）”，“RL”是“强化学习（RL）”，但用户摘要里已经用了缩写，可能需要保留。确保核心创新点如黑盒数据合成、蒸馏成可训练模型、RL中的奖励设计都被涵盖。 </think> 【问题】Vision-language模型作为闭环机器人代理需工具接口控制代码生成，但开放权重VLM转化为高性能具身代理面临工具接口交互失败、黑盒教师模型权重不可访问、监督模仿受分布偏移限制三重挑战；【方法】提出EmbodyAgent框架通过|
|**2026-11-16**|**Competent Autonomous Driving Through Fine Tuning Vision Language Action Models with Symbolic Traffic Rules**|Barkin Dagda et.al.|[2611.20648](http://arxiv.org/abs/2611.20648)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结一篇论文。首先，用户的要求很明确，要用中文，按照【问题】【方法】，总字数控制在300字以内，并且要突出核心创新点，避免技术细节。用户还特别强调严格按照格式输出，所有内容在同一行，不要换行符，不要其他解释。  首先，我需要仔细阅读用户提供的论文摘要，理解其核心内容。论文标题是“通过符号化交通规则微调视觉语言行动模型实现胜任的自动驾驶”，摘要里提到VLA模型在自动驾驶中的应用，但准确预测动作不保证遵守交通规则。论文提出的方法是将符号化的交通规则反馈到策略优化中，结合监督微调和强化学习，用PyReason将英国公路代码转化为可执行的逻辑规则，覆盖速度适应、保持车距和道路用户优先级。评估结果显示在CARLA模拟器上，规则通过率从92.9%提升到97.6%，没有违反优先级规则的情况。  接下来，我需要按照用户给的格式来组织内容。问题部分要简明扼要，指出VLA模型在遵守交通规则上的不足。方法部分要突出核心创新点，即符号化规则反馈和监督强化学习结合，以及使用PyReason处理规则。结论部分要强调结果，提升的合规性和准确率。  需要注意避免技术细节，比如具体的CARLA模拟器、三个RL方法的具体名称等，用户要求不包含这些。同时要确保总字数在300字以内，所以需要精简语言，合并信息。例如，将“监督微调”和“强化学习优化”合并为“监督微调与强化学习优化结合”，用“符号化交通规则”代替“用PyReason将英国公路代码转化为可执行的逻辑规则”。  最后检查格式是否符合要求，所有内容在同一行，没有换行符，严格按照【问题】【方法】，【结论】的顺序，并且没有多余的解释。确保核心创新点突出，比如符号化规则反馈和评估结果。确认字数是否在限制内，可能需要多次调整措辞来压缩字数。 </think> 【问题】VLA模型在自动驾驶中难以确保遵守交通规则；【方法】融合符号化交通规则反馈与监督强化学习优化，将英国公路代码编码为可执行逻辑规则，通过视觉语言模型提取场景特征评估行动后果；【结论】规则通过率|
|**2026-11-16**|**Fuzzy Explainable Continual Hierarchical Reinforcement Learning for Robotic Navigation**|Peng Qin et.al.|[2611.20427](http://arxiv.org/abs/2611.20427)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结一篇论文。首先，我要仔细阅读用户的要求，确保完全理解。用户希望用中文，按照【问题】【方法】，总字数控制在300字以内，并且严格按照指定的格式输出，不能有换行符或其他解释。  论文的标题是Fuzzy Explainable Continual Hierarchical Reinforcement Learning for Robotic Navigation。摘要里提到，持续机器人导航需要强化学习策略在适应新环境的同时保留已有知识，而可解释的强化学习要学习有意义的代表行为。但这两个目标有冲突，因为持续学习强调策略稳定性，而可解释性需要自适应探索。现有方法很少同时处理这两个问题。论文提出了FECHRL方法，分两阶段行为克隆策略，平衡快速适应和可解释行为演化，从强模仿指导过渡到自主强化学习。还用了模糊critic基于T-S模糊系统，缓解值外推错误，提高训练稳定性。实验证明在序列多场景导航中有效统一了持续学习和可解释性，保持知识保留和有意义的解释。  接下来，我需要按照用户给的模板来总结：问题、方法、结论。核心创新点要突出，避免技术细节。问题部分要说明持续学习与可解释性的冲突。方法部分要提到两阶段行为克隆和模糊critic。结论部分强调统一框架，稳定保留知识和可解释行为。  要注意字数限制，确保不超过300字。同时，用户要求所有内容在同一行内，没有换行符，所以需要检查格式是否正确。可能还需要调整用词，使语言更精简，比如“解决持续学习与可解释性冲突”而不是详细描述问题。确保每个部分的关键词都准确，比如“两阶段行为克隆策略”、“T-S模糊系统”等。  最后，检查是否符合所有要求：格式正确，无多余内容，核心创新点突出，字数合适。确认无误后，输出结果。 </think> 【问题】持续机器人导航需平衡环境适应与知识保留，但强化学习政策稳定性与可解释行为探索存在冲突；【方法】提出FECHRL框架，采用两阶段行为克隆策略（初期强模仿指导过渡至自主学习）结合T-S模糊系统构建的模糊critic缓解值外推误差；【结论】实现持续学习与可解释性统一，在多场景实验中达成稳定知识保留和可解释行为演化|
|**2026-11-15**|**Cleanly-DINO: Efficiently Learning Visual Task Spaces for Robotics**|Adrian Röfer et.al.|[2611.20137](http://arxiv.org/abs/2611.20137)|null|<think> 好的，我现在需要帮用户总结这篇论文，按照他们的格式要求。首先，我得仔细阅读用户提供的论文摘要，找出核心问题和方法。  论文标题是“Cleanly-DINO: Efficiently Learning Visual Task Spaces for Robotics”，摘要里提到的问题是，传统的任务学习依赖物体姿态变化，比如抓取，但像清洁这样的任务更多是视觉状态的变化，所以任务表示不明确。方法部分，他们提出了Cleanly-DINO，使用任务相关区域掩码和冻结的ViT特征，通过投影隔离任务空间，然后拟合进展指标。还提到了在真实机器人擦拭流程中的应用。  用户要求突出核心创新点，避免技术细节，控制在300字以内，严格按照问题、方法、结论的格式，同一行，无换行。需要确保不遗漏关键点，比如任务空间的视觉状态变化、投影隔离、进展指标、跨领域应用和实际部署。  可能需要注意术语的简化，比如“projection”翻译为“投影”，“progression metric”是“进展指标”。还要检查是否符合字数限制，可能需要精简语言，比如“评估其定位不完整任务区域和跨视觉领域泛化能力”这样更简洁。  最后确认格式是否正确，没有换行，所有内容在一行，问题、方法、结论用中文，不包含其他解释。确保核心创新点如视觉状态任务空间、投影隔离、进展指标、跨领域和实际应用都涵盖进去。 </think> 问题：传统机器人任务学习依赖物体姿态变化，清洁类任务需从视觉状态变化中抽象任务空间存在表示不明确问题；方法：提出Cleanly-DINO，基于任务相关区域掩码和冻结ViT特征，通过投影隔离任务空间并拟合进展指标，评估其定位不完整任务区域和跨视觉领域泛化能力，应用于强化学习作为观察编码器和奖励信号，并在真实机器人擦拭流程中验证执行指导效果；结论：有效实现清洁任务视觉空间学习，支持跨域迁移和实际部署。|
|**2026-11-05**|**Latent RL Priors for Data-Efficient Dexterous Manipulation**|Yixiao Wang et.al.|[2611.08458](http://arxiv.org/abs/2611.08458)|null|
|**2026-11-05**|**Reinforcing End-to-End Autonomous Driving Safety via Negative-Aware Planning in a Unified World-Action Model**|Zihao Zhang et.al.|[2611.08111](http://arxiv.org/abs/2611.08111)|null|
|**2026-11-05**|**TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation**|Yijiong Lin et.al.|[2611.07881](http://arxiv.org/abs/2611.07881)|null|
|**2026-11-04**|**Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement**|Michal Korniak et.al.|[2611.06905](http://arxiv.org/abs/2611.06905)|null|
|**2026-11-04**|**Dynamic Shape Control of Soft Trunk Robots**|Hehui Zheng et.al.|[2611.06625](http://arxiv.org/abs/2611.06625)|null|
|**2026-11-04**|**H^2MARL: Hierarchical Heterogeneous Multi-agent Reinforcement Learning for Humanoid Robot Control**|Xuemin Hu et.al.|[2611.06523](http://arxiv.org/abs/2611.06523)|null|
|**2026-11-04**|**TwinBridge: Digital Twin-Driven Policy and Reward Transfer for Real-World Reinforcement Learning in Laboratory Robotics**|Shu'ang Sun et.al.|[2611.06442](http://arxiv.org/abs/2611.06442)|null|
|**2026-11-03**|**WayTrace: A Map-to-Language-to-Trace Hierarchy for Embodied Urban Navigation**|Manthan Patel et.al.|[2611.05129](http://arxiv.org/abs/2611.05129)|null|
|**2026-11-03**|**CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation**|Po-Yi Wu et.al.|[2611.05080](http://arxiv.org/abs/2611.05080)|null|
|**2026-11-03**|**LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation**|Hong Je-Gal et.al.|[2611.04974](http://arxiv.org/abs/2611.04974)|null|
|**2026-11-02**|**BeyondContact: A Reinforcement Learning Framework for Airflow-Based Non-Contact Manipulation**|Peiyu Yang et.al.|[2611.03059](http://arxiv.org/abs/2611.03059)|null|
|**2026-10-29**|**MUSBRIC: LEGO-Compatible Pneumatic Muscle Bricks for Reconfigurable Musculoskeletal Robots**|Qiyao Wang et.al.|[2610.40285](http://arxiv.org/abs/2610.40285)|null|
|**2026-10-29**|**Event2Reward: Learning Robotic Rewards from Progress Relations**|Junnan Nie et.al.|[2610.39212](http://arxiv.org/abs/2610.39212)|null|
|**2026-10-28**|**Robotic Data Inoculation**|Qiyang Li et.al.|[2610.39054](http://arxiv.org/abs/2610.39054)|null|
|**2026-10-15**|**Value as Memory: Online Value-Guided Post-training for General Robot Policies**|Wenye Yu et.al.|[2610.22368](http://arxiv.org/abs/2610.22368)|null|
|**2026-10-15**|**Sim-to-Real Reinforcement Learning for Path-Safe Target Reaching in Robotic Harvesting of Hydroponic Lettuce**|Al Bashir et.al.|[2610.22337](http://arxiv.org/abs/2610.22337)|null|
|**2026-10-07**|**HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion**|Mike Zhang et.al.|[2610.10489](http://arxiv.org/abs/2610.10489)|null|
|**2026-10-07**|**Decoding Neural Population Dynamics through Robotic Analog**|Wenhui Chen et.al.|[2610.09977](http://arxiv.org/abs/2610.09977)|null|
|**2026-09-25**|**See to Reach, Feel to Grasp: Learning A Blind Grasp Reflex for Anthropomorphic Robotic Hands**|Alexander Alexiev et.al.|[2609.31323](http://arxiv.org/abs/2609.31323)|null|
|**2026-09-24**|**Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning**|Sudip Bhujel et.al.|[2609.30258](http://arxiv.org/abs/2609.30258)|null|
|**2026-09-24**|**Res-HIL: Human-Guided Residual Reinforcement Learning for Sample-Efficient Dexterous Manipulation**|Mariia Iavorskaia et.al.|[2609.30023](http://arxiv.org/abs/2609.30023)|null|
|**2026-09-22**|**ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model**|Sinuo Wang et.al.|[2609.26299](http://arxiv.org/abs/2609.26299)|null|
|**2026-09-18**|**From Pretraining to Proficiency: Real-World Subtask RL for Long-Horizon Manipulation with Minimal Human Intervention**|Sichang Su et.al.|[2609.21788](http://arxiv.org/abs/2609.21788)|null|
|**2026-09-18**|**Potential-Field Action Representation for Reinforcement Learning in Contact-Rich Manipulation**|Xinyu Liu et.al.|[2609.21609](http://arxiv.org/abs/2609.21609)|null|
|**2026-09-17**|**MILER: Semantic Mid-Level Representation for Sim-to-Real Reinforcement Learning in Unstructured Autonomous Driving**|Thomas Steinecker et.al.|[2609.20747](http://arxiv.org/abs/2609.20747)|null|
|**2026-09-17**|**Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction**|Songyang Liu et.al.|[2609.20558](http://arxiv.org/abs/2609.20558)|null|
|**2026-09-17**|**Visual Sim-to-Real Learning for Robotic Insertion under Geometric Variations: Application to Rebar Installation**|Tao Sun et.al.|[2609.20477](http://arxiv.org/abs/2609.20477)|null|
|**2026-09-17**|**A Mathematical Model of Motivated Emotional Mind - Cognitive Embodied System**|Wiesław L. Galus et.al.|[2609.20437](http://arxiv.org/abs/2609.20437)|null|
|**2026-09-17**|**AnyViewDex: View-Invariant Dexterous Manipulation from RGB Observations**|Soham Patil et.al.|[2609.20107](http://arxiv.org/abs/2609.20107)|null|
|**2026-09-16**|**Learning Holistic Whole-Body Loco-Manipulation with a Bipedal Mobile Manipulator**|Zhongyu Chen et.al.|[2609.18930](http://arxiv.org/abs/2609.18930)|null|
|**2026-09-16**|**KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation**|Sitong Chen et.al.|[2609.18869](http://arxiv.org/abs/2609.18869)|null|
|**2026-09-16**|**M $^3$ P-R1: Reinforcement Learning for Large Language Model Guided Multi-Modal Motion Planning via MIP Code Generation**|Xingpeng Sun et.al.|[2609.18669](http://arxiv.org/abs/2609.18669)|null|
|**2026-09-16**|**FIERCE: From Generalist Robot Policies to Fast Specialists via Progress-Failure Feedback**|Runjia Tan et.al.|[2609.18651](http://arxiv.org/abs/2609.18651)|null|
|**2026-09-15**|**FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence**|Yinhao Li et.al.|[2609.17210](http://arxiv.org/abs/2609.17210)|null|
|**2026-09-15**|**Fingers as Legs: Learning Self-Supported Locomotion and Manipulation with an Anthropomorphic Hand**|Amirhossein Kazemipour et.al.|[2609.17172](http://arxiv.org/abs/2609.17172)|null|
|**2026-09-09**|**HaWMPO: Hallucination-Aware World Model-based Policy Optimization for Generalist Robot Policy**|Zengjue Chen et.al.|[2609.09941](http://arxiv.org/abs/2609.09941)|null|
|**2026-09-04**|**Human-Human & Human-Robot Interaction Transformer (H2INT) for Robot Navigation in Dense and Uncertain Crowds**|Ao Shen et.al.|[2609.05300](http://arxiv.org/abs/2609.05300)|null|
|**2026-09-04**|**Morphology and actuation as inductive biases in robotic hand manipulation**|Zalán Tari et.al.|[2609.05206](http://arxiv.org/abs/2609.05206)|null|
|**2026-08-27**|**Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation**|Wendong Li et.al.|[2608.27158](http://arxiv.org/abs/2608.27158)|null|
|**2026-08-27**|**GRAFT: Grounded and Efficient Online Reinforcement Adaptation for Fine-Grained Robot Manipulation**|Yibo Qiu et.al.|[2608.27079](http://arxiv.org/abs/2608.27079)|null|
|**2026-08-26**|**$R^3$ : Training Robots to Reason in Natural Language via Reinforcement Learning**|Lehong Wu et.al.|[2608.26053](http://arxiv.org/abs/2608.26053)|null|
|**2026-08-24**|**Reward-Free Continual Adaptation for Resilient Space Robots**|Andrej Orsula et.al.|[2608.23452](http://arxiv.org/abs/2608.23452)|null|
|**2026-08-24**|**Distributed Trajectory Planning and Resource Allocation for Dynamic Multi-UAV Collaborative Computing**|Tiankui Zhang et.al.|[2608.23123](http://arxiv.org/abs/2608.23123)|null|
|**2026-08-21**|**Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning**|Varun Giridhar et.al.|[2608.21204](http://arxiv.org/abs/2608.21204)|null|
|**2026-08-21**|**Teaching is a Process: The TOSS Framework for Modeling Human Teaching Decisions in Human-Interactive Robot Learning**|Bernhard Hilpert et.al.|[2608.21083](http://arxiv.org/abs/2608.21083)|null|
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
|**2026-11-19**|**UniVEP: Unifying Velocity and Endpoint Prediction for Robot Manipulation**|Zhengtu Liang et.al.|[2611.26103](http://arxiv.org/abs/2611.26103)|null|<think> 好的，我现在需要帮用户用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我得仔细阅读用户提供的论文摘要，抓住核心内容。  论文标题是UniVEP，主题是统一预测速度和端点来优化机械臂操作。问题部分应该指出传统方法只用单一预测目标的问题，比如恢复噪声动作和优化清洁动作的挑战不同，但现有方法没有效统一处理。方法部分要提到他们比较了三种预测方式，发现不同场景下效果不同，然后提出UniVEP，联合训练并动态切换预测目标，同时加入一致性监督。结论部分要说明测试结果，比如在StarVLA和LiLa-WAM上表现更好，成功率和效率提升，特别是RoboTwin上的数据对比。  需要注意用户强调要突出核心创新点，避免技术细节。所以不能深入解释为什么X--V在少步生成中更好，或者协方差谱的变化，而是直接点出比较结果和提出的解决方案。同时格式必须严格，问题、方法、结论各占一行，同一行内，无换行，不用其他解释。  现在检查字数，确保不超过300字。可能需要调整用词，比如“系统比较”改为“比较”更简洁。确认每个部分的关键点都涵盖，没有遗漏重要数据，比如61.36%的成功率和77.1%的延迟降低。最后确保没有换行符，用空格分隔，符合用户要求。 </think> 问题：传统机器人操作政策在动作生成中单一使用速度或端点预测目标，未有效应对噪声恢复与动作优化不同挑战；方法：比较三种预测模式（V/X/X--V）发现动态切换预测目标及联合训练能提升性能，提出UniVEP通过一致性监督联合训练速度与端点预测并自动切换策略，单步推理即可实现端点恢复与速度修正；结论：在StarVLA/LiLa-WAM上实现更优成功率（61.36% vs 59.96%）与77.1%推理延迟降低，联合训练同步提升单步端点生成效果。|
|**2026-11-19**|**PAD: Policy-Aware Data Valuation for Autonomous Driving**|Chengkai Xu et.al.|[2611.25604](http://arxiv.org/abs/2611.25604)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结一篇论文。首先，我要仔细阅读用户的要求，确保完全理解。用户希望用中文，按照【问题】【方法】，总字数控制在300字以内，并且严格按照指定的格式输出，所有内容在同一行内，不能有换行符或其他解释。  首先，我需要解析论文的摘要内容。论文标题是PAD: Policy-Aware Data Valuation for Autonomous Driving。摘要中提到，自动驾驶系统依赖演示数据的扩展，但数据增长并不必然带来政策提升。现有方法通常通过内在样本属性或训练依赖的代理指标来评估数据价值，但这些不衡量下游政策效用。因此，作者提出了PAD框架，通过场景级校准反馈、投影政策梯度以及本地训练几何的近似，为每个候选演示分配特定于目标驾驶政策的效用值。实验部分显示，PAD在不同规划器上表现优于仅使用真实数据，并显著减少场景级回归问题。  接下来，我需要将问题和方法提炼出来。问题部分要突出数据积累不直接提升政策效果，现有方法评估数据价值不基于下游政策效用。方法部分要说明PAD的核心创新，即结合校准反馈、投影梯度和几何近似，生成可扩展的影响值，并针对不同规划器进行策略优化。  需要注意用户强调要突出核心创新点，避免技术细节。所以需要简化描述，比如“投影政策梯度”可以简化为“结合政策梯度反馈”，而“本地训练几何的近似”可以简化为“训练几何优化”。同时，确保总字数在限制内，可能需要多次调整措辞。  然后检查格式是否符合要求，确保没有换行符，所有内容在同一行，严格按照【问题】【方法】的结构。最后，确认字数是否在300字以内，可能需要进一步压缩，比如将“通过场景级校准反馈与投影政策梯度结合，并优化训练几何”改为更简洁的表达。  最后，验证是否所有要求都满足，特别是格式和字数限制，确保输出正确无误。 </think> 【问题】自动驾驶数据积累不直接提升政策效果且现有数据估值方法未衡量下游政策效用【方法】提出政策感知数据估值框架PAD，通过场景级校准反馈与投影政策梯度结合，并优化训练几何生成可扩展的政策影响值，实现差异化数据筛选【结论】PAD使多类规划器在NavTest和NavHard任务|
|**2026-11-16**|**Competent Autonomous Driving Through Fine Tuning Vision Language Action Models with Symbolic Traffic Rules**|Barkin Dagda et.al.|[2611.20648](http://arxiv.org/abs/2611.20648)|null|<think> 好的，我现在需要帮用户总结这篇论文。首先，用户的要求很明确，要用中文精简总结，严格按照问题、方法、结论的格式，控制在300字以内，突出核心创新点，避免技术细节，并且所有内容要在一行内，不换行，不包含其他解释。  首先，我得仔细阅读论文的摘要，找出问题的核心。摘要里提到VLA模型虽然能统一处理感知、推理和控制，但准确预测动作并不保证遵守交通规则。所以问题应该是VLA模型在遵守交通规则上的不足。  接下来是方法部分。论文提出的方法是结合监督微调和使用强化学习优化，引入符号化的交通规则反馈。具体来说，他们用英国道路代码的规则，用PyReason转化为可执行的逻辑规则，然后通过冻结的视觉语言模型提取场景谓词，结合车辆状态评估候选动作的后果。评估用了CARLA模拟器的离线数据，比较了三种RL方法。  结论部分，结果显示方法提升了动作预测准确性和规则遵守率，最佳方案将规则通过率从92.9%提升到97.6%，且零违规。这说明符号规则反馈能有效提升VLA的政策对齐。  现在需要把这些浓缩成问题、方法、结论三个部分，每部分用中文，不超过300字。要注意避免技术细节，比如具体用PyReason和CARLA这些可能属于技术细节，但用户要求突出创新点，所以可能需要保留PyReason作为符号化规则的工具，而CARLA可能可以简略。另外，用户要求直接输出，所以不能有任何解释，严格按照格式。  检查是否符合要求：是否在同一行，有没有换行符，是否包含其他内容。可能需要多次调整，确保字数足够精简，同时涵盖所有关键点。例如，问题部分要明确点出VLA模型在遵守交通规则上的不足；方法部分要说明结合监督微调和强化学习，符号规则反馈，以及评估方式；结论部分强调提升的百分比和零违规的结果。  最后，确保所有内容连贯，没有技术术语堆砌，突出创新点，比如符号规则反馈和RL结合，以及评估结果的有效性。可能还需要调整用词，比如“融合”代替“结合”更正式，但用户可能接受。确认总字数是否在300以内，现在看起来应该没问题。 </think> 问题：Vision-language-action models缺乏有效交通规则约束导致自动驾驶政策偏离规范|
|**2026-11-10**|**From Prediction to Action: Learning Physical Context for Deformable Linear Object Manipulation**|Chengxiao Dong et.al.|[2611.14274](http://arxiv.org/abs/2611.14274)|null|
|**2026-11-10**|**DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning**|Huaijin Pi et.al.|[2611.14092](http://arxiv.org/abs/2611.14092)|null|
|**2026-11-05**|**Latent RL Priors for Data-Efficient Dexterous Manipulation**|Yixiao Wang et.al.|[2611.08458](http://arxiv.org/abs/2611.08458)|null|
|**2026-11-05**|**MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation**|Sateesh Kumar et.al.|[2611.08372](http://arxiv.org/abs/2611.08372)|null|
|**2026-11-05**|**Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement**|Wenbo Huang et.al.|[2611.08318](http://arxiv.org/abs/2611.08318)|null|
|**2026-11-05**|**Transformer-Based Trajectory Prescription for sEMG-Optimizing Robot-Mediated Rehabilitation**|Gabriel Parra et.al.|[2611.08295](http://arxiv.org/abs/2611.08295)|null|
|**2026-11-05**|**Reinforcing End-to-End Autonomous Driving Safety via Negative-Aware Planning in a Unified World-Action Model**|Zihao Zhang et.al.|[2611.08111](http://arxiv.org/abs/2611.08111)|null|
|**2026-11-05**|**Learning Robotic World Models with Semantic and Visual Feedback**|Hao Wu et.al.|[2611.07850](http://arxiv.org/abs/2611.07850)|null|
|**2026-11-05**|**Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents**|Jisen Lei et.al.|[2611.07825](http://arxiv.org/abs/2611.07825)|null|
|**2026-11-04**|**Which Physical Tactile Cues Matter for Contact-Rich Imitation Learning? A Controlled Real-Robot Study**|Xuhao Qin et.al.|[2611.06673](http://arxiv.org/abs/2611.06673)|null|
|**2026-11-03**|**Correct Robots Before They Make Mistakes: Proactive Human-in-the-Loop Intervention via Preference Learning**|Xinkai Jiang et.al.|[2611.05667](http://arxiv.org/abs/2611.05667)|null|
|**2026-11-03**|**Spectrally Routed Diffusion Policy for Multi-Task Robotic Manipulation**|Mingcong Li et.al.|[2611.04477](http://arxiv.org/abs/2611.04477)|null|
|**2026-11-02**|**Visuo-tactile Diffusion Policy for Robotic Manipulation with Auxiliary Tactile Dynamics Prediction**|Kaihong Ouyang et.al.|[2611.02677](http://arxiv.org/abs/2611.02677)|null|
|**2026-10-29**|**SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing**|Yunchu Zhang et.al.|[2610.40646](http://arxiv.org/abs/2610.40646)|null|
|**2026-10-29**|**AcrossDEX 1.0: From Human Motion Pretraining to Bimanual Dexterous Manipulation across Hand Embodiments**|Xiaoyu Yang et.al.|[2610.40210](http://arxiv.org/abs/2610.40210)|null|
|**2026-10-29**|**Learning Safe Flow Matching Robot Policies from Binary Feasibility Oracles**|Jianming Ma et.al.|[2610.40075](http://arxiv.org/abs/2610.40075)|null|
|**2026-10-29**|**RAIBO-Wagon: Real-Time Navigation System for a Legged Robot Towing a Wagon**|Insung Yang et.al.|[2610.39267](http://arxiv.org/abs/2610.39267)|null|
|**2026-10-22**|**Revisiting Distribution Matching for State-to-Vision Policy Distillation in Laparoscopic Robotic Manipulation**|Mingyu Sheng et.al.|[2610.31010](http://arxiv.org/abs/2610.31010)|null|
|**2026-10-15**|**MOSS: Mode-Oriented Source Shaping for Robot Flow Matching Policies**|Zirun Ma et.al.|[2610.22193](http://arxiv.org/abs/2610.22193)|null|
|**2026-10-15**|**Trajectory-based Diffusion from One-shot Human Video for Generalizable Manipulation**|Guoping Pan et.al.|[2610.21792](http://arxiv.org/abs/2610.21792)|null|
|**2026-10-11**|**$Δ$ Flow Matching for Robot Foundation Models**|Kuangji Zuo et.al.|[2610.15794](http://arxiv.org/abs/2610.15794)|null|
|**2026-10-11**|**SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation**|Angen Ye et.al.|[2610.15766](http://arxiv.org/abs/2610.15766)|null|
|**2026-10-11**|**Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic JEPA Predictors**|Yeonseok Lee et.al.|[2610.15556](http://arxiv.org/abs/2610.15556)|null|
|**2026-10-07**|**RoboPrompt: Intuitive Robot Policy Steering with Sparse Human Input**|Yanwen Zou et.al.|[2610.10534](http://arxiv.org/abs/2610.10534)|null|
|**2026-10-01**|**Robot Learning on Discrete Surfaces: Theory and Applications**|Matteo Dalle Vedove et.al.|[2610.01910](http://arxiv.org/abs/2610.01910)|null|
|**2026-09-25**|**Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulation via Interaction-Centric Modeling**|Guanlin Li et.al.|[2609.31207](http://arxiv.org/abs/2609.31207)|null|
|**2026-09-25**|**Impedance Cloning: Learning Equilibrium Point Parameters for Contact-Rich Manipulation**|Hayato Takahashi et.al.|[2609.30842](http://arxiv.org/abs/2609.30842)|null|
|**2026-09-25**|**RoboMonitor: Label-Efficient Runtime Monitoring of Robot Task Execution via Predictive Representation Learning**|Abhiroop Ajith et.al.|[2609.30715](http://arxiv.org/abs/2609.30715)|null|
|**2026-09-25**|**Can a Robot Read Braille? - Learning to Adapt Contact via Imitation Learning for Tactile Braille Recognition**|Xi Chen et.al.|[2609.30676](http://arxiv.org/abs/2609.30676)|null|
|**2026-09-24**|**Res-HIL: Human-Guided Residual Reinforcement Learning for Sample-Efficient Dexterous Manipulation**|Mariia Iavorskaia et.al.|[2609.30023](http://arxiv.org/abs/2609.30023)|null|
|**2026-09-24**|**MorphIK: Morphology-Conditioned Neural Inverse Kinematics for Unknown Robots**|Lennart Clasmeier et.al.|[2609.29908](http://arxiv.org/abs/2609.29908)|null|
|**2026-09-24**|**Self-Supervised Anchoring of Fingertip Sensing to Proprioception and Proactive Actions for Robot Imitation Learning**|Tomohiro Motoda et.al.|[2609.29822](http://arxiv.org/abs/2609.29822)|null|
|**2026-09-24**|**PolyUMI: Accessible Visual-Tactile-Audio Data Collection for Object Inference and Manipulation**|Conor W. Hayes et.al.|[2609.29760](http://arxiv.org/abs/2609.29760)|null|
|**2026-09-23**|**AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios**|Zhipeng Bao et.al.|[2609.28366](http://arxiv.org/abs/2609.28366)|null|
|**2026-09-23**|**Distillation for Efficient Multitask Manipulation Policies via Conditional Flow Matching**|Shreya Deshmukh et.al.|[2609.28107](http://arxiv.org/abs/2609.28107)|null|
|**2026-09-22**|**Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation**|Hao Wei et.al.|[2609.26672](http://arxiv.org/abs/2609.26672)|null|
|**2026-09-22**|**ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model**|Sinuo Wang et.al.|[2609.26299](http://arxiv.org/abs/2609.26299)|null|
|**2026-09-22**|**History-Conditioned Flow Matching for Probabilistic Dynamics of Tendon-Driven Continuum Robots**|Hang Yang et.al.|[2609.25658](http://arxiv.org/abs/2609.25658)|null|
|**2026-09-22**|**MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence**|Haoran Wen et.al.|[2609.25627](http://arxiv.org/abs/2609.25627)|null|
|**2026-09-22**|**From Instrument-Mounted Demonstrations to In-Vivo Execution: Learning Bimanual Laparoscopic Appendectomy Without Robot-Collected Demonstrations**|Dongho Yee et.al.|[2609.25625](http://arxiv.org/abs/2609.25625)|null|
|**2026-09-22**|**RoboMP-DINOv2: Prompts, Not Filters for Robust Robot Manipulation**|Han Qi et.al.|[2609.25506](http://arxiv.org/abs/2609.25506)|null|
|**2026-09-18**|**MAAP: Multi-Agent Active Perception for Collaborative Manipulation**|Bruno N. Y. Chen et.al.|[2609.21929](http://arxiv.org/abs/2609.21929)|null|
|**2026-09-18**|**From Pretraining to Proficiency: Real-World Subtask RL for Long-Horizon Manipulation with Minimal Human Intervention**|Sichang Su et.al.|[2609.21788](http://arxiv.org/abs/2609.21788)|null|
|**2026-09-18**|**Towards Fine-Grained Object Manipulation: SAM3-Guided Visuomotor Policy with Persistent Memory Learning and Focused Visual Conditioning**|Haolong Meng et.al.|[2609.21621](http://arxiv.org/abs/2609.21621)|null|
|**2026-09-18**|**Robotic Multiphase Interaction: Manipulating Coupled Liquid and Solid Dynamics with a World Model**|Yixuan Feng et.al.|[2609.21448](http://arxiv.org/abs/2609.21448)|null|
|**2026-09-18**|**Stabilizing Trajectory Outputs in End-to-End Autonomous Driving via SC-IMM Based Teacher Signals**|Siewoo Kim et.al.|[2609.21404](http://arxiv.org/abs/2609.21404)|null|
|**2026-09-17**|**StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation**|Jinbang Huang et.al.|[2609.20791](http://arxiv.org/abs/2609.20791)|null|
|**2026-09-17**|**Agile-WAM: An Agile Tactile World Action Model for Contact-Rich Robot Control**|Hanchu Zhou et.al.|[2609.20761](http://arxiv.org/abs/2609.20761)|null|
|**2026-09-17**|**HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface**|Zimu Han et.al.|[2609.20659](http://arxiv.org/abs/2609.20659)|null|
|**2026-09-17**|**TraceFlow: Guiding Frozen Flow-Matching Robot Policies with Success and Failure Traces**|Jiaxuan Zhang et.al.|[2609.20646](http://arxiv.org/abs/2609.20646)|null|
|**2026-09-17**|**Towards High-DoF Dexterous Manipulation through VLA Post-Training**|Junlei Zhu et.al.|[2609.19666](http://arxiv.org/abs/2609.19666)|null|
|**2026-09-17**|**ReShoot: Generative Visual Domain Randomization of Recorded Robot Demonstrations for Visuomotor Policy Learning**|Chiyoung Kim et.al.|[2609.19661](http://arxiv.org/abs/2609.19661)|null|
|**2026-09-16**|**Learning Holistic Whole-Body Loco-Manipulation with a Bipedal Mobile Manipulator**|Zhongyu Chen et.al.|[2609.18930](http://arxiv.org/abs/2609.18930)|null|
|**2026-09-16**|**WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories**|Yuna Oikawa et.al.|[2609.18435](http://arxiv.org/abs/2609.18435)|null|
|**2026-09-15**|**Dissecting Motion-Prior Regularization for Data-Scarce Robotic Insertion**|Ning Hu et.al.|[2609.17484](http://arxiv.org/abs/2609.17484)|null|
|**2026-09-15**|**SAVLA: Symmetry-Aware Vision-Language-Action Models for Robotic Manipulation**|Junle Li et.al.|[2609.16641](http://arxiv.org/abs/2609.16641)|null|
|**2026-09-09**|**MotionCanvas: Learning Implicit Motion Planning from Composable Kinematic Cues**|Zeyu Ling et.al.|[2609.10457](http://arxiv.org/abs/2609.10457)|null|
|**2026-09-04**|**Towards Neuro-Symbolic Procedural Reasoning for Long-Horizon Vision-Language-Action Manipulation**|Vivek Chavan et.al.|[2609.05369](http://arxiv.org/abs/2609.05369)|null|
|**2026-09-04**|**HaptiNet: Networked Haptic Robots Enable Physical Co-presence in Geographically-Unconstrained Rehabilitation**|Chenyang Sun et.al.|[2609.04799](http://arxiv.org/abs/2609.04799)|null|
|**2026-09-04**|**Dressing in Motion: A Human Motion-Aware Diffusion Policy for Robot-Assisted Dressing**|Haoxiang Sun et.al.|[2609.04759](http://arxiv.org/abs/2609.04759)|null|
|**2026-09-03**|**A Low-Cost, Open Platform for End-to-End Autonomous Driving on a Miniature Ackermann Vehicle**|Gustavo Claudio Karl Couto et.al.|[2609.04147](http://arxiv.org/abs/2609.04147)|null|
|**2026-09-03**|**MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?**|Kohei Sendai et.al.|[2609.03715](http://arxiv.org/abs/2609.03715)|null|
|**2026-09-01**|**Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation**|Haoyuan Deng et.al.|[2609.01596](http://arxiv.org/abs/2609.01596)|null|
|**2026-09-01**|**Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds**|Clinton Enwerem et.al.|[2609.01453](http://arxiv.org/abs/2609.01453)|null|
|**2026-08-30**|**AcrossWAM1.0:A Modular Latent World-Action Stack for Compact Robot Policies**|Yafei Zhang et.al.|[2608.29937](http://arxiv.org/abs/2608.29937)|null|
|**2026-08-30**|**Self-Aware Active Learning Enables Continual Improvement in Autonomous Driving**|Dong Hu et.al.|[2608.29772](http://arxiv.org/abs/2608.29772)|null|
|**2026-08-27**|**Diffusion Policies for Short-Horizon Planning in Robot Crowd Navigation**|Wendong Li et.al.|[2608.27158](http://arxiv.org/abs/2608.27158)|null|
|**2026-08-26**|**$R^3$ : Training Robots to Reason in Natural Language via Reinforcement Learning**|Lehong Wu et.al.|[2608.26053](http://arxiv.org/abs/2608.26053)|null|
|**2026-08-26**|**VISTA: Visually Inferred Spatial ConTact Attention for Contact-Rich Manipulation**|Jiayi Chen et.al.|[2608.25872](http://arxiv.org/abs/2608.25872)|null|
|**2026-08-24**|**MomADv2: Reliable Temporal Memory for End-to-End Autonomous Driving**|Ziying Song et.al.|[2608.23405](http://arxiv.org/abs/2608.23405)|null|
|**2026-08-24**|**Triplet2Track: A Hierarchical System with Object-Centric Representations for Reliable Long-Horizon Manipulation**|Jianxiang Liu et.al.|[2608.22800](http://arxiv.org/abs/2608.22800)|null|
|**2026-08-23**|**WorldToken: Time-First Sequence Modeling for Robotic Imitation Learning**|Chunkai Yang et.al.|[2608.22591](http://arxiv.org/abs/2608.22591)|null|
|**2026-08-21**|**WA-JEPA: Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving**|Xinlin Wang et.al.|[2608.20974](http://arxiv.org/abs/2608.20974)|null|
|**2026-08-21**|**Rethinking Demonstration Unlearning in Imitation Learning for Robotics**|Jiazhuo Li et.al.|[2608.20784](http://arxiv.org/abs/2608.20784)|null|
|**2026-08-21**|**ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation**|Siyuan Ma et.al.|[2608.20735](http://arxiv.org/abs/2608.20735)|null|
|**2026-08-20**|**RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement Learning in Robotic Manipulation**|Shaoxuan Wang et.al.|[2608.20208](http://arxiv.org/abs/2608.20208)|null|
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

