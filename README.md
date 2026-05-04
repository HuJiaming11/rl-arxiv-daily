## Updated on 2026.05.04
> Usage instructions: [here](./docs/README.md#usage)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#reinforcement-learning>Reinforcement Learning</a></li>
    <li><a href=#imitation-learning-&-sft>Imitation Learning & SFT</a></li>
  </ol>
</details>

## Reinforcement Learning

|Publish Date|Title|Authors|PDF|Code|摘要|
|---|---|---|---|---|---|
|**2026-05-01**|**Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies**|Yi Wang et.al.|[2605.00416](http://arxiv.org/abs/2605.00416)|null|<think> 好的，我现在需要帮用户总结这篇论文，按照他们给的格式：问题、方法、结论，控制在300字以内。首先，我得仔细阅读用户提供的论文摘要，抓住核心内容。  论文标题是“Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies”。摘要里提到，虽然大规模预训练对通用机器人策略有帮助，但离线数据不足，部署中会遇到分布偏移、长尾故障、任务变化和人类纠正机会。所以问题应该是通用机器人策略在真实部署中存在离线数据不足的问题，导致无法有效应对各种挑战。  接下来是方法部分。他们提出了LWD框架，结合自主运行和人类干预的数据，通过持续学习改进策略。核心创新点包括使用DIVL和QAM来稳定学习，DIVL处理价值估计，QAM用于策略提取。需要突出这些方法，避免技术细节，比如具体的技术名称可能需要保留，但不要深入解释。  结论部分提到在16台双臂机器人上验证，成功率达95%，尤其在长任务上有显著提升。要强调结果，尤其是成功率和任务类型。  用户要求严格按照格式，所有内容在同一行，没有换行，所以需要用分号分隔。还要注意字数，确保不超过300字。需要检查是否有冗余信息，比如具体任务例子可能可以简化，比如“包括语义杂货补货和长任务”即可。  现在组合起来：问题部分说明离线数据不足和部署中的挑战；方法部分介绍LWD框架，DIVL和QAM；结论部分结果和成功率。确保语言精简，核心创新点突出，比如“自主运行+人类干预”、“DIVL+QAM”这些关键词。  检查是否符合所有要求：格式正确，无换行，字数控制，技术细节适当保留但不过多。可能需要调整用词，比如“离线到在线强化学习框架”更准确。确认后输出。 </think> 问题：通用机器人策略依赖大规模预训练但离线数据不足导致部署中存在分布偏移、长尾故障、任务变化和人类纠正挑战；方法：提出LWD框架通过自主运行与人类干预闭环学习，结合DIVL稳定价值估计和QAM策略提取优化VLA行动生成器；结论：在16台机器人八类任务中单策略持续提升至95%成功率，长任务效果显著增强。|
|**2026-04-29**|**ATLAS: An Annotation Tool for Long-horizon Robotic Action Segmentation**|Sergej Stanovcic et.al.|[2604.26637](http://arxiv.org/abs/2604.26637)|null|<think> 好的，我现在需要帮用户总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，并且突出核心创新点，避免技术细节。  先看一下论文的摘要。问题部分主要讲的是现有的标注工具在处理长时机器人动作分割时存在不足，比如只针对视觉数据、不支持同步的多模态时间序列信号、适配不同数据集格式困难。方法部分介绍了ATLAS工具，支持多模态数据同步可视化，处理ROS bags和RLDS等格式，还有模块化扩展和键盘界面提升效率。结论部分提到实验显示效率提升和准确性提高。  用户需要精简总结，所以需要把问题和方法的核心点提炼出来。问题要突出长时机器人动作标注的挑战，现有工具的局限性。方法要强调ATLAS的多模态支持、格式兼容性、模块化扩展和高效界面。结论部分要总结实验结果，比如效率提升和准确性提高。  需要注意不要用技术细节，比如具体的百分比数据可能可以简化，但用户给的例子中提到了6%和2.8%，可能需要保留关键数字。不过用户要求避免技术细节，所以可能只需要说“显著提升”之类的。但原例子中的回答保留了百分比，可能用户希望保留关键数据。需要确认。  另外，用户要求严格按照格式，所有内容在同一行，没有换行符。所以必须确保结构正确，字数在限制内。现在需要检查字数，确保不超过300字。可能需要多次调整措辞，比如“多模态数据同步可视化”可以简化为“多模态同步可视化”等。  现在开始组织语言：  问题：长时机器人动作标注需求高，现有工具存在视觉数据局限、多模态不支持、适配困难等问题。  方法：ATLAS工具提供多模态同步可视化，支持ROS bags等格式，模块化扩展，高效键盘界面。  结论：实验显示效率提升6%，边界误差降低五倍，时间对齐提高2.8%。  检查字数，确保符合要求。可能需要调整用词，比如“多模态”改为“多模态数据”，“支持”改为“兼容”等。确保核心创新点突出，比如多模态、格式兼容、模块化、高效界面。然后组合成符合格式的句子。 </think> 【问题】长时机器人动作标注需求高但现有工具|
|**2026-04-28**|**KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning**|Yixuan Huang et.al.|[2604.25788](http://arxiv.org/abs/2604.25788)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结这篇论文。首先，用户的要求很明确，要用中文，严格按照问题、方法、结论的格式，总字数控制在300字以内，还要突出核心创新点，避免技术细节，直接输出，不能换行。  首先，我得仔细阅读论文摘要，抓住关键点。论文标题是KinDER，一个机器人学习与规划的物理推理基准。摘要里提到机器人系统需要处理自身、环境和任务带来的运动学、动力学约束。他们提出了KinDER，包含25个生成的环境，兼容Gym的Python库，参数化技能和演示，以及13个基线评估套件，覆盖任务规划、模仿学习、强化学习等方法。环境分五个核心挑战：空间关系、多物体非抓取操作、工具使用、组合几何约束、动态约束，这些与感知、语言理解无关。实验显示现有方法很多环境无法解决，说明现有方法有缺陷，还做了虚实结合的实验，最后开放源码。  接下来要总结成问题、方法、结论。问题部分要说明当前机器人物理推理的挑战和现有方法的不足。方法部分突出KinDER的设计，比如生成的环境、评估套件、五个核心挑战的分离。结论强调实验结果和开放源码的意义。  需要注意用户要求避免技术细节，比如具体的25个环境或13个基线可能不需要详细说明，而是概括为“多模态评估框架”或“标准化评估套件”。核心创新点在于环境设计分五个独立挑战，以及虚实实验验证。要确保语言精简，符合字数限制。  现在检查是否符合格式：问题、方法、结论，同一行，无换行，不包含其他解释。可能需要调整用词，比如“ procedurally generated environments”翻译为“生成式环境”，“disentangled from perception”翻译为“与感知解耦”。确保每个部分不超过字数，比如问题部分可能需要压缩，如“机器人系统需解决物理约束问题，现有方法存在显著缺陷”。  最后，整合所有信息，确保不超过300字，并严格按照用户格式输出。可能需要多次调整，比如将“标准化评估套件”简化为“标准化评估框架”，或者“多模态评估”来涵盖不同方法。确保结论部分提到虚实实验和开源，突出实际应用价值。 </think> 问题：机器人系统需解决物理约束问题，现有方法|
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

<p align=right>(<a href=#updated-on-20260504>back to top</a>)</p>

## Imitation Learning & SFT

|Publish Date|Title|Authors|PDF|Code|摘要|
|---|---|---|---|---|---|
|**2026-05-01**|**MSACT: Multistage Spatial Alignment for Stable Low-Latency Fine Manipulation**|Xianbo Cai et.al.|[2605.00475](http://arxiv.org/abs/2605.00475)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照【问题】【方法】，总字数控制在300字以内。首先，我得仔细阅读论文的摘要，理解核心内容。  论文的问题在于现实中的精细操作，尤其是双臂操作，需要低延迟控制和稳定的视觉定位，但收集大数据成本高，且有限示范会导致定位偏移。现有方法各有取舍：比如ACT通过动作分块提高效率和低延迟，但依赖密集视觉特征且缺乏空间一致性；生成方法如扩散策略虽然表达性强，但采样延迟高；而视觉语言和体素方法虽然通用性和几何定位好，但计算成本高。  接下来看方法部分。作者提出MSACT，即多阶段空间对齐方法。核心创新点包括多阶段空间注意力模块，提取稳定的2D注意力点，并用时间对齐损失预测未来注意力序列。基于ACT和预训练的ResNet视觉先验，将任务相关的2D注意力点作为局部空间模态用于动作预测。同时引入自监督目标，通过对齐未来帧的视觉特征来抑制偏移，无需关键点注释，提升视觉到动作映射的稳定性，尤其是在数据有限的情况下。  结论部分需要总结成果。实验在ALOHA平台上进行，结果显示在任务成功率、注意力偏移、推理延迟和抗视觉干扰方面都有提升，同时保持低延迟。  现在要确保总结符合用户要求：突出核心创新点，避免技术细节，严格按照格式，同一行内，无换行，不包含其他解释。需要检查字数是否在300字以内，并且结构正确。可能需要注意术语的简化，比如“自监督目标”可以简化为“自监督学习”，但用户给的例子中用了“自监督 objective”，所以可能需要保留原词。另外，确保不遗漏任何核心点，如多阶段模块、时间对齐损失、ResNet先验、自监督抑制偏移等。最后检查格式是否正确，没有多余换行或符号。 </think> 【问题】现实精细操作需低延迟与稳定视觉定位，但数据收集成本高且有限示范导致定位漂移，现有方法在效率、表达性与稳定性间存在取舍；【方法】提出MSACT，通过多阶段空间注意力模块提取稳定2D注意力点并联合预测未来序列，引入时间对齐损失抑制漂移，基于ACT与预训练ResNet视觉|
|**2026-05-01**|**Stereo Multistage Spatial Attention for Real-Time Mobile Manipulation Under Visual Scale Variation and Disturbances**|Xianbo Cai et.al.|[2605.00471](http://arxiv.org/abs/2605.00471)|null|<think> 好的，我需要帮用户总结这篇论文，按照他们的格式要求。首先，用户给了一个具体的论文标题和摘要，要求用中文精简总结，分问题、方法、结论三部分，总字数控制在300字以内，还要突出核心创新点，避免技术细节。  首先，我需要仔细阅读论文摘要，找出核心问题和方法。问题部分应该包括视觉尺度变化和干扰对机器人操作的影响。方法部分要提到立体多阶段空间注意力机制和分层递归架构。结论部分则是实验结果，比如鲁棒性和任务成功率提升。  用户强调要严格按照格式，所有内容在同一行，不换行，不加其他解释。所以我要确保结构正确，用【】括起来，每个部分简洁。同时注意字数，不能超过300字。可能需要多次精简，比如把“通过分层递归架构”简化为“分层递归架构”，去掉不必要的细节。  还要检查有没有技术术语，用户要求避免技术细节，所以可能需要简化一些术语，比如“视觉语言行动基线”可以保留，但确保读者能理解。核心创新点在于立体多阶段空间注意力和预测时间建模的结合，这点要突出。  最后，确保输出格式正确，没有换行符，所有内容紧凑。可能需要调整用词，比如“任务相关空间注意力点”简化为“任务相关空间注意力点”或者更简练的表达。检查字数是否符合要求，可能需要多次调整。 </think> 【问题】机器人移动操作中视觉尺度变化和干扰导致任务成功率下降；【方法】提出立体多阶段空间注意力机制与分层递归架构的预测学习法，通过提取立体图像任务相关空间注意力点融合机器人状态实现闭环动作预测；【结论】在四类真实场景实验中显著提升鲁棒性及任务成功率，较主流模仿学习和视觉语言行动基线表现更优。|
|**2026-05-01**|**Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies**|Yi Wang et.al.|[2605.00416](http://arxiv.org/abs/2605.00416)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结一篇论文。首先，我得仔细阅读用户的要求，确保完全理解。用户希望用中文，严格按照【问题】【方法】，总字数控制在300字以内，并且突出核心创新点，避免技术细节。  论文标题是“Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies”。摘要里提到的问题包括大规模预训练虽然有效，但离线数据不足以应对现实部署中的分布偏移、长尾故障、任务变化和人类纠正机会。方法部分介绍了LWD框架，结合自主巡检和人类干预，使用DIVL和QAM来稳定学习。结论是在16台机器人上的验证，成功率95%，尤其长任务提升明显。  接下来，我需要按照用户指定的格式，将问题、方法、结论浓缩到同一行，不超过300字。要突出核心创新点，比如LWD框架、闭环学习、DIVL和QAM的结合，以及实际应用效果。同时避免技术细节，比如具体的算法名称可能需要简化，但用户示例中保留了DIVL和QAM，所以可能需要保留。  检查字数，用户给的示例总结是：“【问题】离线数据无法应对现实部署中的分布偏移、长尾故障、任务变化和人类纠正；【方法】提出LWD框架，通过自主巡检和人类干预形成闭环，结合DIVL稳定价值估计和QAM提取策略；【结论】在16台机器人8项任务中，通用政策成功率95%，长任务提升显著。” 这个大约有200多字，符合要求。  需要确认是否所有关键点都涵盖：问题中的挑战，方法中的闭环和两个技术点，结论中的结果和长任务效果。同时确保没有换行，同一行内，用中文，严格按照格式。用户可能希望直接输出，不需要额外解释，所以必须严格按照指示执行。  最后，检查是否有冗余或可以简化的地方，比如“Fleet-Scale”翻译为“多机舰队”是否合适，或者保持原术语。用户示例中用了“多机舰队”，所以可能更倾向于中文翻译。确认无误后，生成最终答案。 </think> 【问题】离线数据无法应对现实部署中的分布偏移、长尾故障、任务变化和人类纠正；【方法】提出LWD框架，通过多机舰队自主巡检和人类干预形成|
|**2026-04-28**|**KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning**|Yixuan Huang et.al.|[2604.25788](http://arxiv.org/abs/2604.25788)|null|<think> 好的，我现在需要帮用户精简总结这篇关于KinDER的论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，突出核心创新点，避免技术细节，并且直接输出总结内容，所有内容在同一行内，不要换行，不带其他解释。  首先，我得仔细阅读用户提供的论文摘要和标题。论文标题是“KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning”，摘要里提到他们创建了一个基准测试，用于机器人学习与规划中的物理推理挑战。问题部分应该围绕当前机器人系统在物理推理上的不足，比如现有方法无法有效处理复杂的物理约束。方法部分则是他们如何构建这个基准，包括生成的环境、评估套件等。结论则是说明现有方法的不足和基准的价值。  接下来要确保问题部分准确抓住核心问题，即机器人系统在处理自身结构、环境和任务中的物理约束时存在困难，现有方法不足。方法部分需要突出他们开发的KinDER基准，包含25个生成环境、兼容Gym的库、13种基线评估，以及五个核心挑战的分离。结论部分要指出评估显示现有方法有重大缺口，并强调基准的开源和跨范式比较的重要性。  然后要注意字数限制，必须精简，避免技术细节。比如，提到“procedurally generated environments”可以简化为“生成式环境”，而“Gymnasium-compatible Python library”可以简化为“兼容Gym的Python库”。同时，要确保所有内容在同一行，没有换行符，所以需要用空格分隔各部分。  还要检查是否遗漏了核心创新点，比如环境的设计目的是分离五个核心挑战，这点很重要，必须包含。另外，实体的评估和开源也是关键点，不能漏掉。可能需要注意术语的准确性，比如“disentangled from perception, language understanding”可以简化为“与感知、语言解耦”。  最后，检查格式是否符合要求，严格按照【问题】【方法】，总字数是否在300字以内。可能需要多次调整措辞，确保简洁同时信息完整。例如，将“Empirical evaluation shows that existing methods struggle...”转化为“评估显示现有方法在多数环境中存在显著缺陷”，更简洁。  现在把这些整合成一行，确保各部分用【】括起，用空格分隔，不换行。确认没有多余的解释，只保留核心|
|**2026-04-26**|**Tube Diffusion Policy: Reactive Visual-Tactile Policy Learning for Contact-rich Manipulation**|Teng Xue et.al.|[2604.23609](http://arxiv.org/abs/2604.23609)|null|<think> 好的，用户让我用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我需要仔细阅读论文摘要，抓住核心内容。  问题部分应该指出当前方法的不足。摘要提到现有模仿学习依赖动作分块，这在接触丰富场景中无法快速反应，因为物理不确定性和高频触觉反馈需要即时控制。所以问题就是现有方法在动态环境中的反应不足。  方法部分要突出核心创新点。论文提出Tube Diffusion Policy（TDP），结合扩散模型和管道反馈控制。这里的关键是生成模型构建观察条件反馈流，形成动作管道，允许快速适应。需要避免技术细节，直接说明方法的核心。  结论部分要总结效果。摘要提到TDP在多个基准测试中表现优于现有方法，并在真实实验中验证了鲁棒性，同时减少去噪步骤适合实时控制。需要强调这些结果。  用户要求严格格式，同一行内，不换行，不带其他解释。需要检查字数，确保不超过300字。可能需要调整用词，比如“行动分块”改为“动作分块”，“反应控制”等。要确保每个部分简洁，突出创新点，如“生成模型构建反馈流”、“动作管道”等。  最后检查是否符合所有要求：问题、方法、结论，格式正确，字数控制，没有多余内容。可能需要多次精简，比如合并句子，使用更简短的表达。例如，问题部分可以合并为“现有模仿学习依赖动作分块，难以应对接触丰富场景中的物理不确定性和高频触觉反馈的快速反应需求”。方法部分强调生成模型和管道反馈控制，结论部分提到性能提升和实时应用。 </think> 问题：现有模仿学习依赖动作分块，难以应对接触丰富场景中的物理不确定性和高频触觉反馈的快速反应需求；方法：提出Tube Diffusion Policy，结合扩散模型生成观察条件反馈流构建动作管道实现动态控制；结论：在多个基准测试中性能优于基线，验证了实时高频率触觉反馈下的鲁棒性和低去噪步骤优势。|
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

<p align=right>(<a href=#updated-on-20260504>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/HuJiaming11/rl-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/HuJiaming11/rl-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/HuJiaming11/rl-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/HuJiaming11/rl-arxiv-daily/issues

