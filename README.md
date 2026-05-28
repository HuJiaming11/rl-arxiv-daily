## Updated on 2026.05.28
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
|**2026-05-27**|**Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation**|Jiahe Pan et.al.|[2605.28812](http://arxiv.org/abs/2605.28812)|null|<think> 好的，我需要帮用户总结这篇论文，严格按照要求的格式和字数限制。首先，用户给了一个具体的结构：问题、方法、结论，每部分要突出核心创新点，避免技术细节，控制在300字以内，并且所有内容在同一行，不要换行。  先看论文标题和摘要。问题部分主要讲的是在接触丰富的抓取中，真实世界数据收集困难，现有的仿真到现实的强化学习方法通过简化触觉数据到低维特征，牺牲了数据的丰富性，导致无法有效用于复杂抓取。核心问题就是触觉数据简化导致信息损失，影响复杂任务的表现。  方法部分，论文提出了CoP（质心压力点），基于物理原理的触觉表示，保留密集接触信息同时保持仿真到现实的鲁棒性。还提出了基于可微分动力学的传感器校准方案，无需真实力测量就能估计触点方向。需要突出这两个创新点：CoP的物理基础和校准方法。  结论部分，在两个盲测任务中，CoP条件的策略实现了零样本迁移，优于其他基线。分析显示策略自动编码了任务相关的物理属性，比如物体质量。结论的核心是CoP有效，并且策略能自动学习物理属性。  现在需要将这些浓缩成问题、方法、结论三部分，每部分简洁。注意不要技术细节，比如“不同iable dynamics”可以简化为“可微分动力学校准”。检查字数，确保不超过300字，并且同一行，无换行。  可能的总结结构： 问题：仿真到现实抓取中触觉数据简化导致信息损失，影响复杂任务表现； 方法：提出基于物理的质心压力点（CoP）触觉表示，结合可微分动力学校准传感器； 结论：CoP条件策略实现零样本迁移，自动编码物理属性，优于基线。  检查是否符合要求，核心创新点是否突出，有没有多余细节。确认后按格式输出，同一行，无换行。 </think> 问题：仿真到现实抓取中触觉数据简化导致信息损失，影响复杂任务表现；方法：提出基于物理的质心压力点（CoP）触觉表示，结合可微分动力学校准传感器；结论：CoP条件策略实现零样本迁移，自动编码物理属性，优于基线|
|**2026-05-27**|**SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving**|Kangyu Wu et.al.|[2605.28583](http://arxiv.org/abs/2605.28583)|null|<think> 好的，我需要帮用户精简总结这篇论文，按照指定的格式输出。首先，我得仔细阅读用户提供的论文摘要，理解其中的核心问题和创新方法。  论文标题是SARAD，结合了LLM和强化学习，用于自动驾驶的安全和效率。问题部分应该包括传统DRL的不足和LLMs的实时性问题。方法部分要突出SARAD的创新点，比如用RAG增强的LLM指导决策，注意力鉴别器和碰撞预测模块。结论要说明实验结果，比如在Highway-Env中的性能提升。  用户要求严格控制在300字以内，避免技术细节，突出核心创新。我需要确保每个部分简洁明了，不换行，同一行内完成。检查格式是否正确，问题、方法、结论是否准确对应，有没有遗漏关键点。最后确认字数是否符合要求，没有多余的解释。 </think> 问题：自动驾驶决策面临传统DRL unsafe random exploration和LLM实时性不足的双重挑战；方法：SARAD融合LLM与DRL，采用RAG增强LLM决策并引入注意力鉴别器整合专家知识，设计碰撞预测模块；结论：在Highway-Env中验证SARAD显著提升安全性与效率。|
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

<p align=right>(<a href=#updated-on-20260528>back to top</a>)</p>

## Imitation Learning & SFT

|Publish Date|Title|Authors|PDF|Code|摘要|
|---|---|---|---|---|---|
|**2026-05-27**|**Imitation Learning for Robot Assistance in Open Surgery: A Multi-Policy Evaluation on Suture Following**|Xucheng Wang et.al.|[2605.28736](http://arxiv.org/abs/2605.28736)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照【问题】【方法】，总字数控制在300字以内。首先，我得仔细阅读用户提供的论文摘要，抓住核心内容。  论文的问题是关于机器人辅助开放手术中的缝合法（suture following），具体是抓-拉-释放动作。用户强调要突出创新点，避免技术细节，所以得把重点放在问题和方法上，结论部分也要简明。  接下来，方法部分提到评估了四种不同的模仿学习策略，包括ACT、Diffusion Policy、SmolVLA和π₀，在数据集大小、摄像头视角和背景变化三个临床相关维度上测试。关键创新点应该是π₀在预训练视觉语言模型上的表现，数据效率高，鲁棒性强，轨迹平滑，适合手术流程。还有在部署测试中达到了92%的缝合完成率。  结论部分需要说明这些发现证明了协作机器人辅助在开放手术中的可行性，并指出深度感知和末端执行器设计是临床转化的关键。要注意字数限制，确保每部分简洁，不换行，同一行内完成。检查是否有技术细节可以省略，比如具体的配置数量或帧数，只保留核心数据如92%的完成率。最后确认格式是否符合要求，没有换行符，各部分用【】括起，用中文输出。 </think> 【问题】机器人辅助开放手术中缝合法（抓-拉-释放动作）的协作机器人控制难题，需解决多维度临床场景下的精准跟随问题【方法】评估ACT、Diffusion Policy、SmolVLA、π₀四种模仿学习策略在数据集、视角、背景变化下的表现，发现π₀基于预训练视觉语言模型实现最优数据效率（92%临床缝合完成率）、强抗背景干扰和流畅轨迹【结论】协作机器人手术可行，深度感知与末端执行器设计为临床转化关键|
|**2026-05-27**|**DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving**|Chen Shi et.al.|[2605.28544](http://arxiv.org/abs/2605.28544)|null|<think> 好的，我现在需要帮用户精简总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，并且要突出核心创新点，避免技术细节。直接输出总结，不要换行符和其他解释。  先看论文标题和摘要。标题是DriveWAM，重点在于视频生成先验和可扩展的世界动作建模。摘要里提到，预训练的基础模型对自动驾驶很重要，但现有的视觉语言模型主要用静态图像-文本对，而视频生成模型能捕捉时空动态，更适合驾驶。DriveWAM将预训练的视频扩散Transformer改编为自回归视频动作策略，统一视频和动作流，用联合流匹配目标，保留架构同时适应动作生成。还有场景演化的驾驶引导，用冻结的VLM生成语义意图指导生成。另外有选择性KV内存，通过相关性缓存选择保持内存池 bounded。实验显示性能强，数据扩展到100k片段验证潜力。  接下来要提炼问题和方法。问题应该是现有自动驾驶模型依赖静态图像，缺乏时空动态和动作建模，导致难以扩展。方法包括三个核心点：1）将视频扩散模型改编为自回归动作策略，统一时空流；2）引入场景演化引导，用VLM生成语义意图；3）选择性KV内存优化长期记忆。结论是实验和扩展数据证明了有效性。  现在需要检查是否符合用户要求：核心创新点是否突出，有没有技术细节。比如“联合流匹配目标”可能算技术细节，可以简化为“联合训练目标”或者“统一流训练”。选择性KV内存可以简化为“选择性记忆优化”。确保每个部分不超过300字，同一行，无换行。  最后组合成：问题：自动驾驶依赖静态视觉模型，缺乏时空动作建模与可扩展性。方法：改编视频扩散模型为自回归策略，统一时空流；引入场景演化语义引导；选择性KV记忆优化长期记忆。结论：实验验证有效性和数据扩展潜力。  检查字数，大概在100字左右，符合要求。确保没有技术细节，突出创新点。用户可能希望快速了解论文贡献，所以重点在模型改编、场景引导和记忆优化这三个方法。结论部分提到实验结果和扩展数据，显示潜力。这样应该满足用户需求。 </think> 【问题】自动驾驶依赖静态视觉模型缺乏时空动作建模与可扩展性【方法】改编视频|
|**2026-05-27**|**ProgVLA: Progress-Aware Robot Manipulation Skill Learning**|Seungsu Kim et.al.|[2605.28231](http://arxiv.org/abs/2605.28231)|null|<think> 嗯，用户让我用中文精简总结这篇论文，严格按照【问题】【方法】，总字数控制在300字以内。首先，我需要仔细阅读论文的摘要，找出核心问题和方法。  问题部分，论文提到的是机器人抓取任务中，现有模型在计算资源有限的情况下处理长序列的效率不足，导致成功率和泛化能力差。特别是长任务和多目标任务中表现更差。  方法部分，他们提出了ProgVLA，主要创新点有两个：一是用两阶段Perceiver resampling压缩多模态数据，固定控制token；二是用辅助的进度头通过离线强化学习训练，估计任务进度，结合优势流匹配模仿学习。这两个部分需要突出，避免技术细节。  结论部分需要说明结果，比如模型参数少但效果比大模型好，特别是在长任务和多任务中，同时指出进度头和视觉微调是主要贡献。  用户强调要突出核心创新点，避免技术细节，所以得把压缩和多模态编码、进度头和强化学习结合这些点讲清楚。还要注意格式，严格按照问题、方法、结论，同一行，无换行，不用其他解释。总字数要控制在300以内，可能需要精简语言，比如用“压缩多模态长序列”代替详细描述。检查是否每个部分都涵盖了关键点，没有遗漏重要信息。最后确保语句通顺，符合用户要求。 </think> 【问题】机器人抓取任务中长序列多模态数据处理能力不足，计算资源受限时成功率和泛化能力差，尤其长任务与多目标场景表现更弱【方法】ProgVLA通过两阶段Perceiver resampling压缩多模态数据为固定控制token，结合辅助进度头利用离线强化学习估计任务进度，实现优势流匹配的进度感知模仿学习【结论】0.1B参数模型在长任务和多目标场景超越大基线，进度头与视觉微调是主要贡献，有效提升计算效率与任务适应性|
|**2026-05-26**|**TPS-Drive: Task-Guided Representation Purification for VLM-based Autonomous Driving**|Jiaxiang Li et.al.|[2605.27038](http://arxiv.org/abs/2605.27038)|null|<think> 好的，用户让我用中文精简总结一篇论文，严格按照【问题】【方法】，总字数控制在300字以内。首先，我需要仔细阅读用户提供的论文摘要，理解其中的核心内容。  论文标题是TPS-Drive，主要针对VLM在自动驾驶中的问题，即语义推理与精确3D空间预测的桥梁作用未被有效解决。问题部分应该包括现有方法的两个路径：文本对齐方法导致空间幻觉，密集视觉方法导致表示干扰。方法部分要突出任务导向的表示净化，特别是Agent-Centric Tokenizer，使用3D检测头指导的向量量化，重新分配代码书容量，隔离冗余。结论部分需要提到实验结果，比如碰撞率降低和新的安全记录。  用户要求突出核心创新点，避免技术细节，直接输出总结，并且严格按照格式，同一行内，无换行符。需要检查字数是否在300字以内，同时确保问题、方法、结论分明，没有多余的解释。  现在需要将问题、方法、结论用简洁的语言表达出来，确保每个部分的关键点都涵盖。例如，问题部分要说明现有方法的两个问题和导致的后果；方法部分强调任务导向的表示净化和三个阶段训练；结论部分包括实验验证的结果和性能提升。  最后检查格式是否符合要求，确保没有使用换行符，各部分用方括号括起，中间用竖线分隔，总字数是否达标。可能还需要调整措辞，使其更精炼，同时保持信息完整。 </think> 【问题】Vision-Language Models（VLMs）在自动驾驶中面临语义推理与精确3D空间预测的桥梁缺失问题，现有方法或导致空间幻觉或产生冗余干扰；【方法】提出TPS-Drive框架，通过任务导向的表示净化机制，设计Agent-Centric Tokenizer利用冻结的3D检测头指导的向量量化，重新分配代码书容量聚焦动态目标，结合解耦的推理流程与渐进式三阶段训练；【结论】在nuScenes和NAVSIMv1/v2中实现碰撞率降低与安全记录突破，验证了空间表示优化对自动驾驶规划的有效性。|
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

<p align=right>(<a href=#updated-on-20260528>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/HuJiaming11/rl-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/HuJiaming11/rl-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/HuJiaming11/rl-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/HuJiaming11/rl-arxiv-daily/issues

