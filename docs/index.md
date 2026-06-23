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

## Updated on 2026.06.23
> Usage instructions: [here](./docs/README.md#usage)

## Reinforcement Learning

| Publish Date | Title | Authors | PDF | Code | 摘要 |
|:---------|:-----------------------|:---------|:------|:------|:-------------------------------------|
|**2026-06-21**|**Scalable Multi-Task Data Generation via Reinforcement Learning for Language-Conditioned Bimanual Dexterous Manipulation**|Zechu Li et.al.|[2606.22471](http://arxiv.org/abs/2606.22471)|null|<think> 好的，用户让我用中文精简总结一篇论文，按照【问题】【方法】，总字数控制在300字以内，还要突出核心创新点，避免技术细节。首先，我需要仔细阅读论文的摘要，找出问题的核心和提出的方法。  论文标题是关于使用强化学习生成多任务数据，用于语言引导的双手灵巧抓取。摘要里提到的问题是训练通用政策时缺乏大规模高质量数据，合成数据在仿真中可以解决人类演示视频的不足，比如形态不匹配、物理交互缺失和动作不可行。现有方法基于人类远程操控，任务多样性有限，因为对象中心轨迹匹配忽略了机器人执行的可行性。强化学习虽然 scalable，但受限于手工设计的任务特定奖励。  接下来，方法部分，他们提出了一个系统化的强化学习数据生成流程，包括通用化奖励设计、有效的域随机化，以及语言条件化的任务注释。实验显示生成的数据显著提高了三个任务的泛化能力。  现在需要按照格式【问题】【方法】，突出创新点。问题要简明，方法要说明核心创新，比如通用奖励、域随机化、语言注释。结论可能不需要，因为用户给的模板里没有结论，但用户提供的例子中有结论，可能要看具体要求。不过用户这次的指示是严格按照给出的格式，即【问题】【方法】，所以可能不需要结论部分。  需要注意用户强调要所有内容在同一行，不要换行，不要包含其他解释。所以需要将问题和方法浓缩成两行，每行用【】括起来，中间用空格分隔，总字数控制在300字以内。核心创新点是奖励设计、域随机化、语言注释，以及多任务数据生成。需要确保语言简洁，避免技术细节，比如不提具体实验或模型结构。  可能需要多次调整，确保符合格式和字数要求。例如：  【问题】训练双手灵巧抓取时缺乏大规模高质量数据，现有合成数据方法任务多样性不足且依赖手工奖励设计；【方法】提出基于强化学习的多任务数据生成框架，通过通用奖励设计、域随机化和语言条件化任务注释提升数据质量与多样性，增强政策泛化能力。  检查字数，确保不超过300字，同时突出创新点。可能需要进一步精简，比如“语言条件化任务注释”可以简化为“语言条件化标注”等。确保每个部分都准确反映论文内容，没有遗漏关键点。|
|**2026-06-21**|**FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation**|Kexin Shi et.al.|[2606.22303](http://arxiv.org/abs/2606.22303)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，按照问题、方法、结论的格式，控制在300字以内。首先，我得仔细阅读用户提供的论文摘要，抓住核心内容。  论文标题是FlowDPG，关于在流匹配策略上使用确定性策略梯度（DDPG）的改进。问题部分应该提到现实中的强化学习在机器人操作中的挑战，尤其是流匹配策略的BPTT问题。方法部分要突出FlowDPG的创新点，比如蒸馏框架、两个互补向量，以及避免BPTT。结论部分需要说明实验结果，比如92%的成功率，优于其他方法。  用户要求突出核心创新点，避免技术细节，所以需要简化术语，比如“BPTT-free distillation framework”可以翻译为“无需回传的蒸馏框架”。同时要确保结构正确，严格按照问题、方法、结论的顺序，每部分用方括号括起来，且所有内容在同一行，无换行符。  检查字数，确保不超过300字。可能需要调整用词，比如“数值不稳定性”代替“numerically fragile”，更简洁。最后确认是否符合格式要求，没有多余的解释或换行。 </think> [问题]现实机器人操作强化学习面临流匹配策略训练困难，因需通过BPTT回传多步ODE计算噪声到动作，导致计算成本高且数值不稳定；[方法]FlowDPG设计BPTT-free蒸馏框架，将critic梯度蒸馏为速度场，融合示范驱动的可行性速度和critic驱动的价值修正速度；[结论]在AirPods装配任务中实现92%端到端成功率，优于价值条件、辅助模块适应和伴随梯度方法。|
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
|**2026-06-21**|**ARP: Enhancing Quantized Skill Abstractions via Visual Alignment and Iterative Refinement for Robotic Manipulation**|Yuntian Wang et.al.|[2606.22480](http://arxiv.org/abs/2606.22480)|null|<think> 好的，用户让我总结一篇论文，按照【问题】【方法】，总字数控制在300字以内。首先，我需要仔细阅读论文的摘要，找出核心问题和方法。  论文标题是ARP: Enhancing Quantized Skill Abstractions via Visual Alignment and Iterative Refinement for Robotic Manipulation。摘要里提到，学习长时视-动政策是挑战，现有的基于离散量化的技能模仿学习虽然有效，但存在视觉语义对齐不足和连续动作生成精度问题。ARP的解决方案包括视觉-动作对齐目标和轻量级迭代残差头。  用户要求突出核心创新点，避免技术细节。我需要把问题部分简化为现有方法的不足，方法部分强调ARP的两个创新点。注意格式必须严格按照【问题】【方法】，所有内容在同一行，不换行，不带其他解释。  检查字数，确保不超过300字。可能需要精简语言，比如“离散量化技能表示”代替详细描述。确认问题部分准确，方法部分涵盖视觉对齐和迭代细化，结论部分可能用户没要求，但原问题里有结论部分，但用户给的例子中没有，可能需要看用户的具体指示。根据用户提供的例子，他们可能不需要结论，但根据用户的问题结构，可能需要包括。不过用户给的例子中输出只有问题和方法，所以可能不需要结论。需要再仔细看用户的要求。  用户的问题结构是【问题】【方法】，总字数控制在300字以内，所以可能不需要结论部分。但原问题中的模板有【结论】，但用户可能希望按照他们的例子来，即不包含结论。需要确认用户给的例子，用户提供的例子中输出只有问题和方法，所以可能不需要结论。因此，总结时应只包含问题和方法。  现在组织语言：问题部分要指出现有方法在视觉对齐和动作生成上的不足；方法部分说明ARP的两个创新点。确保核心创新点突出，如视觉对齐、迭代细化，避免技术细节如“共享潜在空间”等。最终检查格式和字数是否符合要求。 </think> 【问题】学习长时视-动政策面临复杂行为技能视觉语义对齐不足和连续动作生成精度低的问题；【方法】ARP通过视觉-动作对齐目标和迭代残差头实现技能细化与精准执行|
|**2026-06-21**|**Do Rigid-Body Simulators Dream of Soft Robots? Learning Contact-Rich Manipulation for Tendon-Driven Continuum Robots**|Chengnan Shentu et.al.|[2606.22397](http://arxiv.org/abs/2606.22397)|null|摘要生成失败：429 Client Error: Too Many Requests for url: https://open.bigmodel.cn/api/paas/v4/chat/completions|
|**2026-06-21**|**FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation**|Kexin Shi et.al.|[2606.22303](http://arxiv.org/abs/2606.22303)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，按照问题、方法、结论的格式，控制在300字以内。首先，我得仔细阅读论文摘要，抓住核心内容。  问题部分：论文提到现实中的强化学习在机械臂操作中困难，尤其是流匹配策略，因为需要反向传播通过时间（BPTT）来处理多步常微分方程，导致计算成本高且数值不稳定。这应该是问题的核心。  方法部分：他们提出了FlowDPG，一种基于确定性策略梯度（DDPG）的方法，通过蒸馏批评家的梯度到速度场，绕过BPTT。结合了示范驱动的速度和批评家驱动的修正，分三点贡献：无BPTT的蒸馏框架、与标准DPPG的联系、在AirPods装配任务中的验证。  结论部分：FlowDPG在长周期、多阶段、双臂组装任务中成功率达到92%，优于其他方法，如价值条件、辅助模块适应和伴随式批评家梯度方法。还有视频和更多结果在项目页面上。  现在需要把这些内容压缩成三个部分，每部分简洁，突出创新点，避免技术细节。注意字数限制，确保同一行，无换行，不包含其他解释。检查是否符合用户格式要求，确保关键点如BPTT绕过、蒸馏框架、成功率和对比结果都涵盖进去。可能需要注意术语的准确翻译，比如“flow matching policies”译为“流匹配策略”，“BPTT”保持缩写。最后确保总字数在300以内，可能需要调整措辞，比如用“突破性”或“显著”来强调效果。 </think> 问题：现实强化学习在机械臂流匹配策略中因BPTT计算成本高且数值不稳定导致训练困难；方法：FlowDPG通过蒸馏批评家梯度至速度场绕过BPTT，结合示范驱动的可行速度与批评家驱动的价值修正，提出无BPTT蒸馏框架并建立与标准DPPG的数学联系；结论：FlowDPG在AirPods双臂装配任务中实现92%端到端成功率，优于价值条件、辅助模块适应等主流方法，提供项目页面视频验证。|
|**2026-06-20**|**CoRDE: Concept-Prior Routed Diffusion Experts for Structural Generalization in Robot Manipulation**|Haidong Huang et.al.|[2606.21935](http://arxiv.org/abs/2606.21935)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结这篇论文。首先，我得仔细阅读用户的要求，确保完全理解。用户希望用中文，严格按照【问题】【方法】，总字数控制在300字以内，并且要突出核心创新点，避免技术细节。  论文标题是CoRDE，主要解决机器人操作中的结构泛化问题。摘要里提到扩散模型在多任务和长周期场景下存在结构泛化不足，梯度冲突，纯数据驱动的MoE方法有路由崩溃和参数爆炸的问题。CoRDE的创新点包括概念编码器指导路由，熵控责任推断，低秩适配的专家池。  用户要求结构是【问题】【方法】，所以我要先明确问题部分。问题应该是多任务长周期下结构泛化不足，梯度冲突，MoE方法的路由崩溃和参数爆炸。方法部分要突出概念编码器、软映射矩阵、熵控责任、低秩适配专家池，以及理论分析和实验结果。  需要注意避免技术细节，比如具体的LoRA实现不需要提，但要说明参数高效。核心创新点包括结构引导的路由机制和低秩适配，这两个是关键。然后要检查字数，确保不超过300字，并且所有内容在同一行，没有换行符。  现在组织语言，确保每个部分简洁。问题部分要涵盖场景、主要挑战和现有方法的问题。方法部分要列出CoRDE的创新点，包括指导机制、责任推断、参数优化，以及理论和实验结果。最后检查格式是否符合要求，有没有多余的解释，确保严格按照用户的格式输出。 </think> 【问题】多任务长周期机器人操作中扩散模型存在结构泛化不足、梯度冲突，纯数据驱动MoE方法面临路由崩溃和参数爆炸挑战【方法】CoRDE通过冻结概念编码器提取语义分布，设计软映射矩阵实现熵控责任推断，结合低秩适配专家池控制参数规模，理论保证路由质量与行为多样性平衡，实验验证其优于基线路由稳定性与生成质量【结论】|
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

