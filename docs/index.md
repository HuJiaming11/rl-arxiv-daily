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

## Updated on 2026.04.24
> Usage instructions: [here](./docs/README.md#usage)

## Reinforcement Learning

| Publish Date | Title | Authors | PDF | Code | 摘要 |
|:---------|:-----------------------|:---------|:------|:------|:-------------------------------------|
|**2026-04-23**|**X2-N: A Transformable Wheel-legged Humanoid Robot with Dual-mode Locomotion and Manipulation**|Yan Ning et.al.|[2604.21541](http://arxiv.org/abs/2604.21541)|null|<think> 好的，我现在需要处理用户的请求，帮他总结一篇论文。首先，我得仔细阅读用户的要求，确保完全理解。用户希望用中文精简总结论文，严格按照【问题】【方法】，总字数控制在300字以内，并且突出核心创新点，避免技术细节。同时，输出格式必须严格按照指定，所有内容在同一行，没有换行符或其他解释。  首先，我得分析论文摘要的内容。论文标题是X2-N，一种双模式运动和操作的变形轮腿人形机器人。摘要里提到的问题有两个：一是传统轮腿机器人使用固定轮作为脚，髋关节自由度低，导致在腿式运动时稳定性和机动性不如平脚人形机器人；二是现有平台缺乏完整的上肢和手臂，限制了灵巧操作能力。  接下来是方法部分。论文提出X2-N机器人，具有高自由度变形能力，可以在人形和轮腿模式间无缝切换。还提出了基于强化学习的整体控制框架，统一控制混合运动、变形和操作。验证了动态滑行、上下楼梯和包裹递送等任务，结果显示高效运动、地形适应性强和稳定的位姿操作。  现在需要将这些信息浓缩，突出核心创新点。问题部分要简明指出传统设计的两个不足。方法部分强调变形能力和强化学习框架。结论需要总结高效、适应性和操作性能，以及实际应用潜力。  需要注意用户要求避免技术细节，所以不能深入解释强化学习如何实现，或者具体DoF的数量。保持简洁，直接点出创新点。同时控制字数，确保不超过300字，并且格式正确，所有内容在同一行，用【】括起来，不换行。  可能遇到的挑战是如何在有限的字数内涵盖所有关键点，同时保持流畅。需要检查是否有冗余信息，比如具体的测试任务（动态滑行、楼梯等）是否必要。根据用户要求，结论部分需要包括结果和潜在应用，所以可能需要保留这些例子以说明有效性，但用更简洁的语言表达。  最后，确保严格按照格式输出，没有多余符号或换行。可能需要多次调整措辞，确保每个部分的信息准确且符合字数限制。例如，问题部分用“固定轮脚与髋部自由度低导致腿行稳定性差，缺失上肢限制操作”来概括两个问题。方法部分则用“提出高DoF变形X2-N实现人形/轮|
|**2026-04-23**|**Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot**|Yucheng Xin et.al.|[2604.21351](http://arxiv.org/abs/2604.21351)|null|<think> 好的，我现在需要帮用户总结一篇论文，按照指定的格式：问题、方法、结论，总共不超过300字，并且要突出核心创新点，避免技术细节。首先，我得仔细阅读用户提供的论文摘要，理解其核心内容。  论文标题是“Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot”，摘要里提到，现有的方法主要是在环境依赖动作上有限，通常强制跟踪刚性轨迹，而忽视了与环境的物理交互。作者观察到人类在非自稳动作中会利用“失重”状态，放松特定关节让身体与环境影响接触，从而稳定身体完成动作。他们的方法包括自动标注策略和动态的“失重机制”（WM），动态决定哪些关节放松到什么程度，同时有效与环境互动。实验在三个任务上测试，结果在仿真和Unitree G1机器人上表现好，无需任务特定调优，泛化性强。结论是填补了精确轨迹跟踪与自适应环境交互的鸿沟，提供了生物学启发的解决方案。  接下来要按照用户的要求，用中文精简总结，严格按照问题、方法、结论的格式，每部分之间用竖线分隔，总字数控制在300字以内。需要突出核心创新点，比如自动标注策略、动态失重机制、无需调优泛化强等。避免技术细节，比如具体的实验任务名称可能不需要详细列出，但可以提到任务类型如坐椅子、躺床、倚墙。  需要检查是否符合格式要求：同一行内，无换行符，不要其他解释。可能需要注意字数，确保不超过限制。例如，问题部分要说明现有方法的不足，方法部分说明创新点，结论部分说明成果和意义。  现在组织语言：  问题：现有方法在环境依赖动作中强制跟踪刚性轨迹，忽视物理交互，导致动作不自然。 方法：提出失重机制（WM）和自动标注策略，动态放松关节以利用环境交互，无需任务调优。 结论：在多种环境中泛化良好，平衡轨迹跟踪与自适应交互，提供生物学启发解决方案。  检查字数，确保每个部分简洁，不超过300字。可能需要调整用词，比如“自动标注策略”可以简化为“自动标注”，“动态确定”改为“动态调整”等。确保核心创新点突出，如动态机制、自动标注、无需调优、泛化强。 </think|
|**2026-04-14**|**Tree Learning: A Multi-Skill Continual Learning Framework for Humanoid Robots**|Yifei Yan et.al.|[2604.12909](http://arxiv.org/abs/2604.12909)|null|【问题】研究如何让人形机器人高效扩展新技能同时避免灾难性遗忘。【方法】1. **根分支层次参数继承机制**：通过参数重用为分支技能提供运动先验，从根本上防止灾难性遗忘 2. **多模态前馈适应机制**：结合相位调制和插值，支持周期性和非周期性运动 3. **任务级奖励塑形策略**：加速技能收敛【结论】Tree Learning在多种代表性运动技能中获得更高奖励，同时保持100%技能保留率，实现无缝多技能切换和实时交互控制。|
|**2026-04-14**|**A hierarchical spatial-aware algorithm with efficient reinforcement learning for human-robot task planning and allocation in production**|Jintao Xue et.al.|[2604.12669](http://arxiv.org/abs/2604.12669)|null|【问题】研究如何解决复杂动态制造环境中人机协作的任务规划与分配问题，特别是如何有效考虑空间信息以提高生产效率。【方法】1. **分层架构**：将任务规划与分配分离，高层负责任务规划，底层负责任务分配。2. **EBQ方法**：基于缓冲区的深度Q学习算法，解决长期稀疏奖励问题，减少训练时间并提升性能。3. **SAP方法**：基于路径规划的空间感知方法，根据人机实时位置和移动距离分配任务资源。【结论】提出的EBQ&SAP方法在复杂动态生产环境中有效解决人机任务规划与分配问题，显著提升生产效率。|
|**2026-04-14**|**Safe reinforcement learning with online filtering for fatigue-predictive human-robot task planning and allocation in production**|Jintao Xue et.al.|[2604.12667](http://arxiv.org/abs/2604.12667)|null|【问题】研究如何动态规划人机任务分配，在保证生产效率的同时确保工人疲劳度在安全范围内。【方法】1. **疲劳参数在线估计**：使用粒子滤波器实时跟踪人类疲劳并更新疲劳模型参数 2. **任务级疲劳预测**：在决策过程中进行疲劳预测，排除超过疲劳限制的任务 3. **约束强化学习**：将问题建模为约束马尔可夫决策过程，结合**受限决斗双深度Q学习**算法实现安全任务分配【结论】PF-CD3Q方法能有效处理疲劳参数的不确定性，在保证工人安全的同时优化生产效率，为工业5.0环境下的人机协作提供实用解决方案。|
|**2026-04-14**|**FeaXDrive: Feasibility-aware Trajectory-Centric Diffusion Planning for End-to-End Autonomous Driving**|Baoyun Wang et.al.|[2604.12656](http://arxiv.org/abs/2604.12656)|null|【问题】端到端扩散规划在自动驾驶中展现出潜力，但生成轨迹的物理可行性仍不足。【方法】1. **轨迹中心化建模**：将清洁轨迹作为扩散过程中可行性感知建模的统一对象 2. **自适应曲率约束训练**：提高内在几何和运动学可行性 3. **可行区域引导**：在反向扩散采样中增强与可行区域的一致性 4. **可行性感知GRPO后训练**：平衡轨迹空间可行性并提升规划性能【结论】FeaXDrive在NAVSIM基准测试中实现了强闭环规划性能，同时显著提升轨迹空间可行性，为更可靠的自动驾驶规划器提供重要进展。|
|**2026-04-14**|**A Comparison of Reinforcement Learning and Optimal Control Methods for Path Planning**|Qiang Le et.al.|[2604.12628](http://arxiv.org/abs/2604.12628)|null|【问题】研究如何解决威胁环境中自主车辆路径规划的计算效率问题，实现实时决策。【方法】1. **深度确定性策略梯度(DDPG)**：结合actor-critic网络结构，直接从状态映射到动作序列 2. **威胁区域建模**：将威胁简化为圆形"禁止进入"区域，作为任务失败条件 3. **可行集计算**：训练DDPG找到能保证安全到达目标的最大起始点集合，为任务规划提供关键信息【结论】DDPG方法比传统最优控制方法更快生成有效路径，更适合实时应用，但存在不可行区域和路径非最优问题，为未来改进指明方向。|
|**2026-04-14**|**Whole-Body Mobile Manipulation using Offline Reinforcement Learning on Sub-optimal Controllers**|Snehal Jauhri et.al.|[2604.12509](http://arxiv.org/abs/2604.12509)|null|【问题】研究如何解决移动操作中机器人的全身协调控制问题，特别是在处理铰接物体时的挑战。【方法】1. **次优全身控制器**：利用次优控制器在状态-动作空间的相关区域收集数据，提供强大的结构先验；2. **两阶段流程**：通过随机化轻量级WBC生成多样化演示，再应用离线RL改进行为；3. **Q-chunking技术**：扩展离线隐式Q-learning，实现块级评估和优势加权策略提取，支持复杂协调任务。【结论】WHOLE-MoMa在模拟和真实机器人上显著优于基线方法，无需遥操作或真实训练数据即可实现高成功率任务。|
|**2026-04-14**|**A Heterogeneous Dual-Network Framework for Emergency Delivery UAVs: Communication Assurance and Path Planning Coordination**|Ping Huang et.al.|[2604.12501](http://arxiv.org/abs/2604.12501)|null|【问题】研究如何确保灾害后无人机应急配送中的可靠指挥控制链路，以应对地面基础设施损坏带来的通信挑战。【方法】1. **异构双网络框架(HDNF)**：结合应急通信支持网络(ECSN)和配送路径网络(DPN)，实现三维覆盖与路径协同；2. **多层C2服务模型**：突破二维限制，将无人机基站部署与关键三维任务阶段对齐；3. **三维覆盖感知多智能体强化学习算法**：解决高维搜索空间问题，提升训练效率和拓扑韧性；4. **三维通信感知A*规划器**：联合优化C2质量和飞行能耗，减少轨迹-覆盖不匹配。【结论】HDNF显著提高了C2可靠性，消除了关键阶段的中断，维持了高任务成功率，同时降低了硬件部署成本。|
|**2026-04-11**|**MoRI: Mixture of RL and IL Experts for Long-Horizon Manipulation Tasks**|Yaohang Xu et.al.|[2604.10165](http://arxiv.org/abs/2604.10165)|null|【问题】研究如何解决强化学习(RL)和模仿学习(IL)在长时程操作任务中的局限性，以及如何有效结合两者的优势。【方法】1. **专家混合机制**：基于专家动作方差动态切换IL和RL专家，处理粗略运动和精细操作 2. **两阶段训练**：采用离线预训练结合在线微调加速收敛 3. **IL正则化**：对RL组件施加IL约束确保探索安全并减少人工干预【结论】MoRI在四个复杂现实任务中实现97.5%的平均成功率，减少85.8%人工干预并缩短21%收敛时间，显著提升机器人操作效率和安全性。|
|**2026-04-10**|**Learning Vision-Language-Action World Models for Autonomous Driving**|Guoqing Wang et.al.|[2604.09059](http://arxiv.org/abs/2604.09059)|null|【问题】现有VLA模型缺乏显式的时间动态建模和全局世界一致性，限制了其前瞻性和安全性；而世界模型虽能模拟未来场景，但难以推理或评估生成的未来。【方法】1. **VLA-World框架**：统一预测性想象和反思推理，提升驾驶前瞻能力；2. **行动引导轨迹生成**：使用行动衍生的可行轨迹指导下一帧图像生成，捕捉环境演化的时空线索；3. **三阶段训练策略**：包括预训练、监督微调和强化学习，并构建nuScenes-GR-20K数据集支持流程。【结论】VLA-World在规划和未来生成基准上 consistently超越最先进的VLA和世界模型基线，提高了性能和可解释性。|
|**2026-04-09**|**LAMP: Lift Image-Editing as General 3D Priors for Open-world Manipulation**|Jingjing Wang et.al.|[2604.08475](http://arxiv.org/abs/2604.08475)|null|【问题】现有机器人学习方法在开放世界场景中难以处理新任务和新环境，缺乏细粒度的3D空间关系理解。【方法】1. **图像编辑作为3D先验**：将2D图像编辑操作提升为3D变换先验，提取对象间的连续几何关系 2. **几何感知表示**：将隐式的2D空间线索显式转换为3D变换，提供细粒度指导 3. **零样本泛化能力**：通过提取的3D变换实现开放世界场景中的零样本泛化，无需特定任务训练【结论】LAMP方法能够精确提取3D变换，在开放世界操作中实现强零样本泛化，为机器人操作提供了新的几何感知解决方案。|
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
|**2026-04-23**|**FingerEye: Continuous and Unified Vision-Tactile Sensing for Dexterous Manipulation**|Zhixuan Xu et.al.|[2604.20689](http://arxiv.org/abs/2604.20689)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结一篇论文。首先，我得仔细阅读用户的要求，确保完全理解。用户希望用中文，严格按照【问题】【方法】，总字数控制在300字以内，突出核心创新点，避免技术细节，直接输出总结内容，格式不能有换行符，也不能有其他解释。  首先看论文标题是FingerEye: Continuous and Unified Vision-Tactile Sensing for Dexterous Manipulation。摘要里提到，现有的触觉传感器如GelSight只能在接触后提供反馈，限制了接触初期的精确操作。他们提出FingerEye，整合了双目RGB相机和可变形环结构，提供连续的视觉和触觉反馈，从接触前到接触后无缝过渡。然后他们用视觉触觉模仿学习政策，结合数字孪生和增强模拟数据来提升泛化能力，最后在多个任务中验证效果。  接下来需要按照用户给的模板来组织内容。问题部分要指出现有传感器的不足，方法部分要说明FingerEye的创新点和解决方法，结论部分则是应用效果和成果。要注意避免技术细节，比如具体的变形结构、标记估计这些可能不需要详细说明，只要提到整合视觉和触觉反馈，以及数字孪生和模拟增强学习即可。  然后检查字数，确保不超过300字。可能需要精简语言，比如“提供连续的视觉-触觉反馈”而不是详细描述每个部分。核心创新点包括连续反馈、视觉触觉融合、数字孪生和模拟数据增强。结论部分要提到在多种任务中的成功应用，比如硬币站立、芯片抓取等，并提到代码和视频开源。  最后确保格式正确，所有内容在同一行，没有换行符，使用用户指定的标签。可能需要多次调整，比如问题部分要简洁，方法部分突出传感器设计和学习方法，结论强调效果和开源资源。检查是否有冗余信息，比如具体任务例子可以保留，但确保整体流畅。 </think> 【问题】现有触觉传感器仅提供接触后反馈，限制机器人精准接触初期操作，缺乏连续感知能力与多模态融合方法；【方法】研发FingerEye传感器集成双目视觉与可变形环结构实现接触前视觉-接触后触觉连续感知，开发融合数字孪生与视觉增强模拟数据的模仿学习政策；【结论】在硬币站立|
|**2026-04-22**|**Stability-Driven Motion Generation for Object-Guided Human-Human Co-Manipulation**|Jiahao Xu et.al.|[2604.20336](http://arxiv.org/abs/2604.20336)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结一篇论文。首先，我得仔细阅读用户的要求，确保完全理解。用户希望用中文，严格按照【问题】【方法】，总字数控制在300字以内，突出核心创新点，避免技术细节，直接输出总结内容，并且所有内容在同一行内，不要换行符。  论文的标题是“Stability-Driven Motion Generation for Object-Guided Human-Human Co-Manipulation”，摘要里提到的问题是现有的协作操作方法在多人协作时考虑不足，比如单角色场景或负载动力学。方法部分提到了流匹配框架，包括生成模型、对抗性交互先验和稳定性驱动的仿真优化。结论是实验结果显示他们的方法在接触精度、穿透率和分布保真度上优于现有方法。  接下来，我需要按照用户指定的格式来组织内容。问题部分要简明扼要，指出现有方法的不足。方法部分要突出核心创新点，比如生成模型、对抗性先验和稳定性仿真。结论要总结实验结果和代码 availability。  需要注意的是用户强调避免技术细节，所以不能深入解释每个部分，而是概括性地陈述。同时要检查字数，确保不超过300字。还要确保所有内容在同一行，没有换行符，这可能需要用空格连接各部分，或者去掉换行符号。  现在开始组织语言。问题部分可以写：“多人协作操作需同步动作与共享物体，但现有方法忽略负载动力学，存在动作不稳定、交互生硬问题”。方法部分：“提出流匹配框架，结合物体功能生成操作策略、对抗性优化自然姿态交互、稳定性仿真调整向量场”。结论部分：“实验验证接触精度高、穿透率低、分布保真度优，代码开源”。  检查字数是否符合，确保格式正确，没有多余的解释。确认无误后，组合成一行，去掉换行符。最后再通读一遍，确保符合用户的所有要求。 </think> 【问题】多人协作操作需同步动作与共享物体，但现有方法忽略负载动力学，存在动作不稳定、交互生硬问题【方法】提出流匹配框架，结合物体功能生成操作策略、对抗性优化自然姿态交互、稳定性仿真调整向量场【结论】实验验证接触精度高、穿透率低、分布保真度优，代码开源|
|**2026-04-15**|**HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System**|Tianshuo Yang et.al.|[2604.14125](http://arxiv.org/abs/2604.14125)|null|【问题】研究如何解决端到端视觉-语言-行动(VLA)模型在窄域控制数据微调时损失基础视觉语言模型(VLM)推理能力的问题。【方法】1. **视觉中心分层框架**：明确解耦高层语义规划与底层电机控制，保留VLM零样本推理能力 2. **VLM规划器**：执行任务分解与视觉 grounding，生成结构化计划(子任务指令和精确目标边界框) 3. **级联交叉注意力DiT**：融合全局上下文、高分辨率物体中心裁剪和技能语义，实现鲁棒执行【结论】HiVLA在仿真和现实实验中显著超越最先进基线，特别擅长长时程技能组合和杂乱场景中小物体的精细操作。|
|**2026-04-14**|**Whole-Body Mobile Manipulation using Offline Reinforcement Learning on Sub-optimal Controllers**|Snehal Jauhri et.al.|[2604.12509](http://arxiv.org/abs/2604.12509)|null|【问题】研究如何解决移动机械臂在操作铰接物体（如开门、抽屉等）时全身协调控制问题，克服传统控制器调参困难和基于学习方法依赖大量遥操作数据的问题。【方法】1. **次优控制器**：利用轻量级次优全身体控制器生成多样化演示数据，在状态-动作空间的相关约束区域内收集数据；2. **离线强化学习**：通过两阶段流程，先随机化轻量级控制器生成演示，再应用离线RL识别并改进行为；3. **Q-chunking技术**：扩展离线隐式Q-learning，实现块级评估和优势加权策略提取，支持复杂协调任务的动作块扩散策略。【结论】WHOLE-MoMa在仿真中显著优于基线方法，成功迁移到真实机器人，无需微调即可实现80%的双手抽屉操作和68%的橱柜开启与物体放置成功率，无需遥操作或真实世界训练数据。|
|**2026-04-13**|**AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation**|Mingyang Li et.al.|[2604.11674](http://arxiv.org/abs/2604.11674)|null|【问题】现有机器人操作数据生成平台未整合物体可操作性信息，导致需要精确交互特定功能区域的任务无法自动生成语义正确的轨迹。【方法】1. **VoxAfford模型**：开放词汇3D可操作性检测器，通过多尺度几何特征增强MLLM输出标记，预测物体点云上的可操作性映射图2. **跨 embodiment 支持**：基于NVIDIA Isaac Sim构建，支持Franka FR3、Panda、UR5e、Kinova等多种机器人平台3. **VLM驱动任务生成**：结合视觉语言模型自动生成多样化操作任务4. **DA3 3D高斯重建**：基于真实照片的域随机化技术，增强模拟环境真实性【结论】AffordSim建立了包含50个跨7类任务的基准，显示当前模仿学习方法在需要精确可操作性的任务（如倒窄口容器和挂钩挂杯）成功率低（0-43%），验证了可感知数据生成的必要性，且零样本模拟到现实实验证明了数据可迁移性。|
|**2026-04-12**|**LIDEA: Human-to-Robot Imitation Learning via Implicit Feature Distillation and Explicit Geometry Alignment**|Yifu Xu et.al.|[2604.10677](http://arxiv.org/abs/2604.10677)|null|【问题】研究如何利用人类视频数据解决机器人演示数据稀缺问题，并克服人类与机器人之间的具身差距。【方法】1. **隐式特征蒸馏**：通过双阶段传递蒸馏管道在共享潜在空间中对齐人类和机器人表示 2. **显式几何对齐**：提出与具身无关的对齐策略，将具身与交互几何解耦，确保一致的3D感知 3. **跨具身转移框架**：结合2D视觉域和3D几何域的对齐方法，实现从人类到机器人的模仿学习【结论】LIDEA框架可替代高达80%的机器人演示数据，并在分布外泛化中成功转移未见模式，显著提升了机器人学习的数据效率和鲁棒性。|
|**2026-04-12**|**OmniUMI: Towards Physically Grounded Robot Learning via Human-Aligned Multimodal Interaction**|Shaqi Luo et.al.|[2604.10647](http://arxiv.org/abs/2604.10647)|null|【问题】现有UMI接口主要依赖视觉和轨迹数据，缺乏物理交互信号，难以处理需要接触动力学的复杂操作。【方法】1. **多模态同步采集**：整合RGB、深度、轨迹、触觉、抓取力和外部交互扭矩等信号，通过紧凑手持系统实现物理数据获取；2. **共享 embodiment 设计**：确保采集与部署一致性，提供双力反馈（夹持器反馈和外部交互扭矩自然感知）；3. **扩散策略扩展**：结合视觉、触觉和力相关观测，基于阻抗执行实现运动与接触行为的统一调控。【结论】OmniUMI通过物理基础的多模态数据采集与人对齐交互，为接触密集型操作学习提供了可扩展基础，在力敏感抓取、交互擦除和触觉选择性释放任务中展现可靠性能。|
|**2026-04-12**|**AffordGen: Generating Diverse Demonstrations for Generalizable Object Manipulation with Afford Correspondence**|Jiawei Zhang et.al.|[2604.10579](http://arxiv.org/abs/2604.10579)|null|【问题】研究如何解决机器人操作中因数据多样性不足导致的几何变化限制问题。【方法】1. **核心概念1**：利用3D生成模型和视觉基础模型(VFMs)大规模生成操作轨迹 2. **核心概念2**：通过大规模3D网格中有意义关键点的语义对应关系实现多样化演示生成 3. **核心概念3**：结合语义可泛化性与端到端学习的反应鲁棒性训练闭环视觉运动策略【结论】AffordGen框架在模拟和真实环境中实现了高成功率，支持对真正未见物体的零样本泛化，显著提高了机器人学习的数据效率。|
|**2026-04-11**|**MoRI: Mixture of RL and IL Experts for Long-Horizon Manipulation Tasks**|Yaohang Xu et.al.|[2604.10165](http://arxiv.org/abs/2604.10165)|null|【问题】研究如何解决强化学习(RL)和模仿学习(IL)在长时程操作任务中的局限性，以及如何有效结合两者优势。【方法】1. **专家混合机制**：基于专家动作方差动态切换IL和RL专家，处理粗略移动和精细操作 2. **离线预训练与在线微调**：先通过离线数据预训练专家模型，再进行在线微调加速收敛 3. **IL正则化**：对RL组件应用IL正则化确保探索安全并减少人工干预【结论】MoRI在四个复杂现实任务中平均成功率达97.5%，相比基线RL算法减少85.8%人工干预并缩短21%收敛时间，有效提升了机器人操作能力。|
|**2026-04-10**|**VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis**|Xiaolei Lang et.al.|[2604.09330](http://arxiv.org/abs/2604.09330)|null|【问题】研究如何高效生成对齐的视频-动作对以解决机器人训练数据收集成本高的问题。【方法】1. **双流框架**：同步生成视频和动作流，确保跨模态一致性 2. **流匹配技术**：基于去噪过程的统一生成方法，实现视频和动作的同步优化 3. **自适应3D池化机制**：将全局视频上下文紧凑传递到动作分支，增强动作生成的准确性【结论】VAG在模拟和真实环境中生成高质量对齐的视频-动作对，支持可执行轨迹回放，并能提升下游策略的泛化能力，为具身数据合成提供实用解决方案。|
|**2026-04-10**|**Learning Vision-Language-Action World Models for Autonomous Driving**|Guoqing Wang et.al.|[2604.09059](http://arxiv.org/abs/2604.09059)|null|【问题】现有视觉-语言-行动模型缺乏时间动态和全局世界一致性建模，限制了预测能力和安全性；而世界模型难以推理或评估生成的未来场景。【方法】1. **VLA-World框架**：整合预测性想象与反思性推理提升驾驶预测能力 2. **行动引导轨迹生成**：使用行动衍生的可行轨迹指导下一帧图像生成，捕捉丰富的时空环境演化线索 3. **三阶段训练策略**：包括预训练、监督微调和强化学习，并构建nuScenes-GR-20K生成推理数据集【结论】VLA-World在规划和未来生成基准上持续超越最先进VLA和世界模型基线，提高了驾驶预测性能和可解释性。|
|**2026-04-09**|**Generative Simulation for Policy Learning in Physical Human-Robot Interaction**|Junxiang Wang et.al.|[2604.08664](http://arxiv.org/abs/2604.08664)|null|【问题】开发自主物理人机交互系统面临大规模训练数据稀缺的挑战，难以学习鲁棒的机器人行为。【方法】1. **零样本"文本到仿真到现实"框架**：从高级自然语言提示自动合成多样化人机交互场景 2. **大语言模型和视觉语言模型**：程序化生成软体人体模型、场景布局和机器人运动轨迹 3. **点云分割的视觉模仿学习**：基于合成数据集训练政策实现零样本仿真到现实迁移【结论】该框架成功应用于抓挠和沐浴两项物理辅助任务，政策成功率超过80%，对非脚本化人体运动具有鲁棒性，首次实现人机交互应用的生成式仿真自动化流程。|
|**2026-04-09**|**LAMP: Lift Image-Editing as General 3D Priors for Open-world Manipulation**|Jingjing Wang et.al.|[2604.08475](http://arxiv.org/abs/2604.08475)|null|【问题】如何实现机器人在开放世界中的类人泛化能力，解决现有方法在 novel 任务和 unseen 环境中的局限性。【方法】1. **图像编辑提升为3D先验**：将图像编辑的2D空间线索转化为3D变换，提供细粒度几何感知指导 2. **连续几何感知表示**：提取物体间3D变换作为连续、几何感知的表示方法 3. **零样本泛化能力**：利用图像编辑中隐含的丰富空间信息，实现开放世界操作的精确指导【结论】LAMP方法通过将图像编辑提升为3D先验，实现了精确的3D变换和开放世界操作中的强零样本泛化，为机器人操作提供了新的解决思路。|
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

