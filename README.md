## Updated on 2026.04.15
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
|**2026-04-14**|**Tree Learning: A Multi-Skill Continual Learning Framework for Humanoid Robots**|Yifei Yan et.al.|[2604.12909](http://arxiv.org/abs/2604.12909)|null|【问题】人形机器人从单任务向多技能学习范式转变时，如何高效扩展新技能同时避免灾难性遗忘是具身智能领域的核心挑战。【方法】1. **根-枝层次参数继承机制**：通过参数重用为分支技能提供运动先验，从根本上防止灾难性遗忘 2. **多模态前馈适应机制**：结合相位调制和插值技术，支持周期性和非周期性运动 3. **任务级奖励塑形策略**：加速技能收敛过程【结论】Tree Learning在各种代表性运动技能中获得更高奖励，同时保持100%技能保留率，实现无缝多技能切换和实时交互控制，显著提升人形机器人多技能学习效率。|
|**2026-04-14**|**A hierarchical spatial-aware algorithm with efficient reinforcement learning for human-robot task planning and allocation in production**|Jintao Xue et.al.|[2604.12669](http://arxiv.org/abs/2604.12669)|null|【问题】研究如何解决复杂动态制造环境中人机协作任务规划与分配(TPA)问题，特别是需要考虑空间信息带来的挑战。【方法】1. **任务分层**：将生产任务分解为可管理的子任务，由高层代理负责任务规划，底层代理负责任务分配 2. **EBQ方法**：提出基于缓冲的高效深度Q学习方法，减少训练时间并解决长期稀疏奖励问题 3. **SAP方法**：设计基于路径规划的空间感知方法，将子任务分配给合适的人机资源【结论】EBQ&SAP方法有效解决了复杂动态生产过程中的人机TPA问题，提高了生产效率，为先进制造系统提供了实用解决方案。|
|**2026-04-14**|**Safe reinforcement learning with online filtering for fatigue-predictive human-robot task planning and allocation in production**|Jintao Xue et.al.|[2604.12667](http://arxiv.org/abs/2604.12667)|null|【问题】研究如何解决人机协作制造中的动态任务规划与分配问题，在保证生产效率的同时确保工人疲劳度在安全范围内。【方法】1. **粒子滤波**：实时跟踪和更新工人疲劳模型参数，处理疲劳参数的不确定性 2. **约束双深度Q学习**：将疲劳预测整合到决策过程中，排除超过疲劳限制的任务，约束动作空间 3. **约束马尔可夫决策过程**：将问题建模为CMDP，确保决策满足疲劳安全约束【结论】PF-CD3Q方法通过实时疲劳预测和约束学习，有效提高了人机协作任务分配的安全性和效率，为工业5.0环境下的人机协作提供了新的解决方案。|
|**2026-04-14**|**FeaXDrive: Feasibility-aware Trajectory-Centric Diffusion Planning for End-to-End Autonomous Driving**|Baoyun Wang et.al.|[2604.12656](http://arxiv.org/abs/2604.12656)|null|【问题】端到端扩散规划在自动驾驶中潜力巨大，但生成轨迹的物理可行性仍不足，存在局部几何不规则、违反运动约束或偏离可行区域等问题。【方法】1. **轨迹中心化建模**：将清洁轨迹作为扩散过程中可行性感知建模的统一对象，而非传统噪声中心化方法 2. **自适应曲率约束训练**：提高轨迹的内在几何和运动可行性，确保轨迹平滑且符合运动学约束 3. **可行区域引导采样**：在反向扩散过程中引入可行区域指导，增强轨迹与可行区域的一致性 4. **可行性感知GRPO后训练**：进一步优化规划性能，平衡轨迹空间可行性与任务目标【结论】FeaXDrive在NAVSIM基准测试中展现出强大的闭环规划性能，同时显著提升轨迹空间可行性，为端到端扩散规划中显式建模轨迹可行性提供了重要方向，推动自动驾驶规划器向更可靠、物理基础扎实的方向发展。|
|**2026-04-14**|**A Comparison of Reinforcement Learning and Optimal Control Methods for Path Planning**|Qiang Le et.al.|[2604.12628](http://arxiv.org/abs/2604.12628)|null|【问题】研究如何解决自主车辆在威胁环境中的实时路径规划问题，传统最优控制方法计算时间过长。【方法】1. **深度确定性策略梯度(DDPG)**：基于强化学习的智能体训练方法，通过状态-动作映射实现安全导航 2. **威胁模型**：将威胁简化为圆形"禁止进入"区域，进入即任务失败 3. **可行集概念**：学习能保证安全到达目标的最大起始点集合，为任务规划提供关键信息【结论】DDPG方法相比传统最优控制显著提升计算速度，适用于实时应用，但存在不可行区域和路径非最优问题，为未来研究指明改进方向。|
|**2026-04-14**|**Whole-Body Mobile Manipulation using Offline Reinforcement Learning on Sub-optimal Controllers**|Snehal Jauhri et.al.|[2604.12509](http://arxiv.org/abs/2604.12509)|null|【问题】研究如何解决移动机械臂在关节物体操作中的全身协调问题，同时克服传统控制器需要大量调参和基于学习方法依赖昂贵数据的问题。【方法】1. **次优控制器**：利用次优全身控制器作为结构先验，在状态-动作空间的任务相关区域收集数据；2. **两阶段流程**：通过轻量级WBC随机化生成多样化演示，再使用离线RL改进行为；3. **Q-chunking技术**：扩展离线隐式Q-learning，实现块级评估和优势加权策略提取，支持复杂协调任务。【结论】WHOLE-MoMa在三个难度递增的任务中显著优于基线方法，策略可直接迁移至真实机器人，无需微调或真实世界训练数据，在双臂抽屉操作和橱柜开合任务中分别达到80%和68%成功率。|
|**2026-04-14**|**A Heterogeneous Dual-Network Framework for Emergency Delivery UAVs: Communication Assurance and Path Planning Coordination**|Ping Huang et.al.|[2604.12501](http://arxiv.org/abs/2604.12501)|null|【问题】研究如何解决灾害后地面基础设施受损情况下应急配送UAV的可靠指挥控制问题。【方法】1. **异构双网络框架(HDNF)**：耦合应急通信支持网络(ECSN)和配送路径网络(DPN)，实现3D覆盖与路径协调 2. **多层C2服务模型**：克服2D度量限制，实现UAV-BS与关键3D阶段部署对齐 3. **3D覆盖感知多智能体强化学习算法**：解决高维搜索空间问题，提高训练效率和拓扑韧性 4. **3D通信感知A*规划器**：联合优化C2质量和飞行能耗，减少轨迹-覆盖不匹配【结论】HDNF显著提高C2可靠性，消除关键阶段中断，维持高任务成功率同时降低硬件部署成本。|
|**2026-04-11**|**MoRI: Mixture of RL and IL Experts for Long-Horizon Manipulation Tasks**|Yaohang Xu et.al.|[2604.10165](http://arxiv.org/abs/2604.10165)|null|【问题】研究如何解决强化学习(RL)和模仿学习(IL)在机器人操作任务中的局限性，结合两者的优势以提高复杂长期任务的成功率。【方法】1. **专家混合机制**：动态切换IL和RL专家基于动作方差，处理粗略运动和精细操作 2. **两阶段训练**：离线预训练后在线微调加速收敛 3. **IL正则化**：对RL组件应用IL正则化确保探索安全并减少人工干预【结论】MoRI在四个复杂现实任务中实现97.5%的平均成功率，相比基线RL算法减少85.8%人工干预和21%收敛时间，显著提升机器人操作效率。|
|**2026-04-10**|**Learning Vision-Language-Action World Models for Autonomous Driving**|Guoqing Wang et.al.|[2604.09059](http://arxiv.org/abs/2604.09059)|null|【问题】现有VLA模型缺乏显式的时间动态建模和全局世界一致性，限制了前瞻性和安全性；传统世界模型虽能模拟未来场景但难以推理或评估生成的未来。【方法】1. **VLA-World框架**：统一预测想象与反思推理，提升驾驶前瞻能力 2. **轨迹引导图像生成**：利用动作派生的可行轨迹指导下一帧图像生成，捕获环境演化的时空线索 3. **自我生成未来帧推理**：对生成的未来帧进行推理以优化预测轨迹，提高性能和可解释性 4. **nuScenes-GR-20K数据集**：基于nuScenes构建的生成推理数据集 5. **三阶段训练策略**：预训练、监督微调和强化学习相结合。【结论】VLA-World在规划和未来生成基准上均超越现有VLA和世界模型基线，显著提升自动驾驶系统的性能和安全性。|
|**2026-04-09**|**LAMP: Lift Image-Editing as General 3D Priors for Open-world Manipulation**|Jingjing Wang et.al.|[2604.08475](http://arxiv.org/abs/2604.08475)|null|【问题】研究如何解决机器人在开放世界环境中面对新任务和新环境时的泛化能力不足问题。【方法】1. **LAMP框架**：将图像编辑技术提升为通用3D先验，提取物体间3D变换作为连续几何感知表示 2. **2D到3D提升**：利用图像编辑中固有的丰富2D空间线索，将其隐含信息转换为3D变换 3. **零样本泛化**：通过提取的精细3D变换指导开放世界操作，实现无需训练的泛化能力【结论】LAMP实现了精确的3D变换提取和开放世界操作中的强零样本泛化效果，为机器人操作提供了新的几何感知解决方案。|
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

<p align=right>(<a href=#updated-on-20260415>back to top</a>)</p>

## Imitation Learning & SFT

|Publish Date|Title|Authors|PDF|Code|摘要|
|---|---|---|---|---|---|
|**2026-04-14**|**Whole-Body Mobile Manipulation using Offline Reinforcement Learning on Sub-optimal Controllers**|Snehal Jauhri et.al.|[2604.12509](http://arxiv.org/abs/2604.12509)|null|【问题】研究如何解决移动操作任务中机器人全身协调控制的难题，传统方法需要大量手工调整且脆弱，而学习方法依赖昂贵遥操作数据或复杂奖励设计。【方法】1. **次优全身控制器**：利用次优控制器在任务相关状态-空间区域收集数据，作为结构先验；2. **两阶段管道**：首先通过随机化轻量级WBC生成多样化演示，再应用离线RL识别并改进行为；3. **Q-chunking技术**：扩展离线隐式Q-learning，实现块级评估和优势加权策略提取。【结论】WHOLE-MoMa在模拟和真实机器人上显著优于基线方法，无需遥操作或真实训练数据即可实现双臂抽屉操作80%成功率，同时打开橱柜和物体放置68%成功率。|
|**2026-04-13**|**AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation**|Mingyang Li et.al.|[2604.11674](http://arxiv.org/abs/2604.11674)|null|【问题】现有机器人操作数据生成平台未整合物体功能区域信息，导致需要精确交互的任务无法自动生成语义正确的轨迹。【方法】1. **VoxAfford模型**：开放词汇3D功能区域检测器，通过多尺度几何特征增强MLLM输出，预测物体点云上的功能区域图2. **跨平台支持**：基于NVIDIA Isaac Sim构建，支持Franka FR3、Panda等多种机器人平台3. **任务生成**：采用视觉语言模型驱动的任务生成和基于DA3的3D高斯重建域随机化【结论】AffordSim建立了包含50个任务的基准测试，显示抓取任务成功率较高(53-93%)，但倒水(1-43%)和挂杯(0-47%)等需要精确功能区域交互的任务仍具挑战，零样本仿真到现实实验验证了数据可迁移性。|
|**2026-04-12**|**LIDEA: Human-to-Robot Imitation Learning via Implicit Feature Distillation and Explicit Geometry Alignment**|Yifu Xu et.al.|[2604.10677](http://arxiv.org/abs/2604.10677)|null|【问题】研究如何利用人类视频数据解决机器人演示数据稀缺问题，同时弥合人类手与机器人手臂之间的具身差距。【方法】1. **双阶段传递蒸馏**：在2D视觉领域，通过共享潜在空间对齐人类和机器人表示 2. **具身无关对齐策略**：在3D几何领域，明确解耦具身与交互几何，确保一致的3D感知 3. **隐式特征蒸馏**：通过隐式特征提取减少视觉差异带来的伪影【结论】LIDEA框架可替代高达80%的昂贵机器人演示数据，并能将人类视频中的未见模式成功转移，实现分布外泛化，显著提升机器人学习的数据效率和鲁棒性。|
|**2026-04-12**|**OmniUMI: Towards Physically Grounded Robot Learning via Human-Aligned Multimodal Interaction**|Shaqi Luo et.al.|[2604.10647](http://arxiv.org/abs/2604.10647)|null|【问题】现有机器人学习系统主要依赖视觉和轨迹数据，缺乏物理交互信号，难以应对接触密集型操作。【方法】1. **多模态同步采集**：整合RGB、深度、轨迹、触觉感知、抓取力和外部交互力矩等物理信号；2. **共享具身设计**：通过紧凑手持系统实现采集-部署一致性；3. **双力反馈机制**：提供双边夹持器反馈和外部交互力矩的自然感知，结合阻抗执行统一调节运动和接触行为。【结论】OmniUMI通过物理引导的多模态数据采集与人类对齐交互，为接触密集型操作提供了可扩展的学习基础，在力敏感抓取、交互擦除和触觉选择性释放等任务中展现可靠性能。|
|**2026-04-12**|**AffordGen: Generating Diverse Demonstrations for Generalizable Object Manipulation with Afford Correspondence**|Jiawei Zhang et.al.|[2604.10579](http://arxiv.org/abs/2604.10579)|null|【问题】现有模仿学习方法在机器人操作中受限于几何变化和有限的数据多样性，导致泛化能力不足。【方法】1. **核心概念1**：利用**3D生成模型**和**视觉基础模型(VFMs)**大规模生成多样化操作轨迹 2. **核心概念2**：通过大规模3D网格中有意义关键点的**语义对应关系**实现新轨迹生成 3. **核心概念3**：构建**感知能力数据集**训练闭环视觉运动策略，结合语义泛化性和端到端学习鲁棒性【结论】AffordGen在模拟和真实环境中实现高成功率，支持对未见对象的零样本泛化，显著提升机器人学习的数据效率。|
|**2026-04-11**|**MoRI: Mixture of RL and IL Experts for Long-Horizon Manipulation Tasks**|Yaohang Xu et.al.|[2604.10165](http://arxiv.org/abs/2604.10165)|null|【问题】研究如何解决强化学习(RL)与模仿学习(IL)在长时程操作任务中的局限性，探索两者有效融合的新方法。【方法】1. **专家混合机制**：基于专家动作方差动态切换IL与RL专家，处理粗略移动和精细操作 2. **两阶段训练框架**：采用离线预训练与在线微调加速收敛 3. **IL正则化技术**：对RL组件施加IL正则化确保探索安全并减少人工干预【结论】MoRI在四项复杂现实任务中实现97.5%平均成功率，相比基线算法减少85.8%人工干预并缩短21%收敛时间，有效提升了机器人操作能力。|
|**2026-04-10**|**VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis**|Xiaolei Lang et.al.|[2604.09330](http://arxiv.org/abs/2604.09330)|null|【问题】如何高效生成对齐的视频-动作对以解决机器人学习数据稀缺问题。【方法】1. **双流框架**：同步生成视频和动作流，确保跨模态一致性 2. **流匹配方法**：基于扩散模型实现联合生成，提高质量与效率 3. **自适应3D池化**：将全局视频上下文紧凑传递至动作分支，增强对齐精度【结论】VAG在仿真和真实环境中生成高质量视频-动作对，支持可执行轨迹回放，提升下游策略泛化能力，为具身数据合成提供实用解决方案。|
|**2026-04-10**|**Learning Vision-Language-Action World Models for Autonomous Driving**|Guoqing Wang et.al.|[2604.09059](http://arxiv.org/abs/2604.09059)|null|【问题】现有VLA模型缺乏时序动态建模和全局世界一致性，限制了预测能力和安全性；而传统世界模型难以推理或评估生成的未来场景。【方法】1. **VLA-World框架**：整合预测性想象与反思推理，通过动作导出的可行轨迹指导下一帧图像生成，捕获时空环境演化信息 2. **自我生成未来帧推理**：对生成的未来帧进行推理以优化预测轨迹，提升性能和可解释性 3. **三阶段训练策略**：包含预训练、监督微调和强化学习，并构建nuScenes-GR-20K数据集支持流水线【结论】VLA-World在规划和未来生成基准上持续超越最先进的VLA和世界模型基线，显著提升了自动驾驶的预测能力和安全性。|
|**2026-04-09**|**Generative Simulation for Policy Learning in Physical Human-Robot Interaction**|Junxiang Wang et.al.|[2604.08664](http://arxiv.org/abs/2604.08664)|null|【问题】研究如何解决物理人机交互(pHRI)系统因大规模训练数据稀缺而难以学习鲁棒机器人行为的问题。【方法】1. **零"text2sim2real"框架**：从高级自然语言提示自动合成多样化pHRI场景 2. **LLMs和VLMs技术**：程序化生成软体人体模型、场景布局和机器人运动轨迹 3. **视觉模仿学习策略**：基于分割点云训练实现零样本仿真到现实迁移【结论】该框架成功实现超过80%的成功率，展现出对非脚本化人体运动的鲁棒性，首次为pHRI应用提供完整的生成式仿真管道，自动化环境合成、数据收集和策略学习。|
|**2026-04-09**|**LAMP: Lift Image-Editing as General 3D Priors for Open-world Manipulation**|Jingjing Wang et.al.|[2604.08475](http://arxiv.org/abs/2604.08475)|null|【问题】研究如何解决机器人在开放世界中的泛化问题，特别是处理新任务和未知环境时的挑战。【方法】1. **图像编辑作为3D先验**：将2D图像编辑操作提升为3D空间变换，提取物体间的3D变换关系 2. **几何感知表示**：利用图像编辑中隐含的2D空间线索，将其转化为连续的3D变换，提供细粒度指导 3. **零样本泛化能力**：通过3D变换表示实现开放世界环境中的零样本泛化，无需特定任务训练【结论】LAMP方法通过将图像编辑提升为3D先验，实现了精确的3D变换和开放世界中的强零样本泛化效果，为机器人操作提供了新的几何感知解决方案。|
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

<p align=right>(<a href=#updated-on-20260415>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/HuJiaming11/rl-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/HuJiaming11/rl-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/HuJiaming11/rl-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/HuJiaming11/rl-arxiv-daily/issues

