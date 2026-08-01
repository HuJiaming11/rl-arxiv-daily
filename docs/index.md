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

## Updated on 2026.08.01
> Usage instructions: [here](./docs/README.md#usage)

## Reinforcement Learning

| Publish Date | Title | Authors | PDF | Code | 摘要 |
|:---------|:-----------------------|:---------|:------|:------|:-------------------------------------|
|**2026-07-30**|**MARS-RA: Rank Aggregation for Credit Assignment via Multimodal Comparisons in Embodied Multi-Agent Cooperation**|Dawei Wang et.al.|[2607.27967](http://arxiv.org/abs/2607.27967)|null|<think> 好的，我现在需要处理用户的请求，帮他精简总结一篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，并且突出核心创新点，避免技术细节。同时，输出格式必须严格，所有内容在同一行，不要换行和其他解释。  首先，我得仔细阅读用户提供的论文摘要。论文标题是MARS-RA，主要解决多智能体强化学习中的信用分配问题。问题部分的关键点在于信用分配在具身AI中的挑战，包括有限和延迟的反馈，以及动态变化的活跃智能体数量。方法部分提到将信用分配转化为排名聚合问题，利用大模态生成的贡献对智能体进行两两比较，然后通过潜在奖励塑造将比较结果转化为贡献分数。结论部分有理论证明和实验结果，显示该方法有效。  接下来，我需要按照用户指定的格式来组织内容。问题部分要简明扼要，突出挑战；方法部分要说明核心创新点，即排名聚合和贡献比较；结论要提到理论和实验支持。同时要确保总字数不超过300字，并且避免技术细节，比如具体的理论证明或实验任务类型。  需要注意的是，用户强调直接输出总结，不要换行，所以必须将所有内容压缩成一行。可能需要多次调整用词，确保简洁。例如，问题部分可以写成“具身多智能体协作中信用分配面临反馈有限、动态参与和噪声干扰挑战”，方法部分则是“将信用分配转化为多模态模型生成的贡献对智能体两两比较的排名聚合问题，通过潜在奖励塑造将比较结果转化为贡献分数”。结论部分则强调理论收敛性、鲁棒性和Shapley值参考，以及实验验证的有效合作。  最后检查是否符合所有要求：格式正确，字数控制，核心创新点突出，无技术细节，无换行和其他解释。确认无误后，就可以输出了。 </think> 【问题】具身多智能体协作中信用分配面临反馈有限、动态参与和噪声干扰挑战【方法】将信用分配转化为多模态模型生成的贡献对智能体两两比较的排名聚合问题，通过潜在奖励塑造将比较结果转化为贡献分数，理论证明收敛性并引入Shapley值参考【结论】在动态多智能体环境中有效提升协作效率，实验验证其鲁棒性和可解释性|
|**2026-07-30**|**Learning Social Robot Navigation By Sensing Human Legs**|Alberto Vaglio et.al.|[2607.27922](http://arxiv.org/abs/2607.27922)|null|<think> 好的，我现在需要帮用户总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，还要突出核心创新点，避免技术细节。而且必须用中文，并且所有内容在同一行，不要换行符。  先看论文标题和摘要。问题部分应该指出当前机器人导航中LiDAR传感器在地面高度只能检测到人的腿部，而现有的学习方法却将行人简化为圆形等简单形状，导致导航效果不佳。方法部分需要提到他们提出的CALF架构，结合卷积层、注意力机制和MLP，直接从LiDAR扫描中解析腿部运动，并通过LegNav模拟器训练强化学习策略。结论部分则是他们的方法在仿真和真实场景中都表现良好，验证了有效性。  接下来要确保核心创新点突出。比如，CALF直接处理腿部数据而不是简化模型，LegNav模拟器的结合使用，以及实际部署的成功。技术细节如JAX或GPU训练时间可以省略，用户要求避免这些。  然后检查格式，确保问题、方法、结论三个部分，用竖线分隔，所有内容在同一行，没有换行符。字数要控制在300字以内，中文表达要简洁。可能需要调整用词，比如“解决机器人通过低空LiDAR感知行人腿部但传统方法简化为圆形的问题”这样更直接。  最后再通读一遍，确认是否符合所有要求，没有遗漏核心点，格式正确，字数合适。确保没有使用任何markdown，纯文本输出。这样应该就能满足用户的需求了。 </think> 【问题】机器人通过低空LiDAR感知行人腿部但传统方法简化为圆形导致导航失效；【方法】提出CALF架构融合卷积注意力机制解析腿部运动并训练轻量级LegNav仿真器；【结论】实现零样本部署在TurtleBot 4上生成合规轨迹，验证多模态感知与强化学习结合的有效性。|
|**2026-07-29**|**SymmGrid: Super-Scaling On-Robot Learning with Parallelized Symmetries and Egocentric-Exocentric Visual Perception**|Gabe Everett et.al.|[2607.26985](http://arxiv.org/abs/2607.26985)|null|摘要生成失败：429 Client Error: Too Many Requests for url: https://open.bigmodel.cn/api/paas/v4/chat/completions|
|**2026-07-29**|**RLMM-Flow: A Flow-based Mobile Manipulation Framework with Latent-Space Reinforcement Learning**|Shuhang Wang et.al.|[2607.26460](http://arxiv.org/abs/2607.26460)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我得仔细阅读用户提供的论文摘要，抓住核心内容。  论文标题是RLMM-Flow，一个基于流的移动抓取框架，结合了潜在空间的强化学习。摘要里提到的问题在于移动抓取需要生成满足多个条件的动作片段，现有的流方法依赖专家示教，但无法超越示教分布的质量。方法部分他们提出了RLMM-Flow，分两步：先预训练流政策捕捉多模态运动先验，然后冻结流政策，用潜在 steering 网络引导噪声到高价值动作。还提到用预热动作空间批评家，以及粗到细的潜在控制。结论是实验证明优于现有方法，同时保持快速推理。  用户要求突出核心创新点，避免技术细节。我需要把问题、方法和结论分别提炼出来，确保每部分简洁。问题部分要说明现有方法的不足，方法部分强调预训练加潜在强化学习的结合，结论突出性能提升和保持推理速度。注意不要换行，所有内容在同一行，用空格分隔。检查字数是否在300以内，确保格式正确。 </think> 问题：移动抓取需生成满足多约束条件的动作片段，现有流方法依赖专家示教且无法突破示教分布局限；方法：RLMM-Flow结合专家流政策预训练与潜在空间强化学习后训练，预训练流政策捕捉多模态运动先验后冻结，通过潜在steering网络引导噪声优化，采用预热动作空间批评家与粗到细潜在控制优化；结论：在移动抓取基准测试中显著提升任务成功率、碰撞规避和轨迹质量，优于现有流方法及强化学习基线，同时保持流快速推理优势。|
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
|**2026-07-30**|**ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine**|Yukang Cao et.al.|[2607.28625](http://arxiv.org/abs/2607.28625)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，并且突出核心创新点，避免技术细节。直接输出总结内容，不换行，不包含其他解释。  首先，我得仔细阅读论文的摘要，抓住问题的核心。摘要里提到，embodied intelligence面临数据瓶颈，现有的数据集碎片化，无法完整捕捉人类在追求目标过程中多模态数据的同步演变。问题应该围绕数据碎片化和感知-行动循环不完整。  接下来是方法部分。论文提出了ACE数据引擎，分为桌级和房级配置，记录多模态数据流，构建ACE-Data-0数据集，包含150小时视频和17M帧，50名参与者，75,000个交互实例。核心创新点在于统一多感官记录和分层基准测试。需要避免技术细节，所以不用提具体记录哪些数据，而是强调多模态同步和分层评估。  结论部分需要说明数据集的优势，比如自然行为变异、同步监督，以及应用领域。但用户要求总字数在300字以内，所以结论要简洁，可能只保留关键点，如填补数据瓶颈，支持多种AI任务。  现在需要检查是否符合格式，问题、方法、结论是否清晰，有没有技术细节，字数是否合适。用户特别强调不要换行，所以必须确保所有内容在同一行。可能需要多次调整，确保核心创新点突出，比如ACE的两个配置、多模态同步、分层基准、填补数据瓶颈等。  最后，检查是否严格按照用户格式，有没有多余的解释，确保总字数控制在300字以内。可能需要删减冗余词汇，比如“人类在追求目标过程中”可以简化为“人类行为”，但需保持原意。确认无误后，输出最终结果。 </think> 【问题】Embodied intelligence面临多模态感知-行动循环数据瓶颈，现有数据集碎片化且缺乏时空同步，无法完整捕捉人类行为中视觉、运动、触觉等多维度动态演化；【方法】创新性设计ACE数据引擎，通过桌级（微观操作）与房级（全身交互）双模态配置同步采集多感官数据流，构建包含150小时视频、75,000交互实例的ACE-Data-0数据集，并建立分层评估基准；【|
|**2026-07-30**|**FA-RDP: A Frequency-Adaptive Reactive Diffusion Policy for Contact-Rich Manipulation**|Lifeng Zhuo et.al.|[2607.28596](http://arxiv.org/abs/2607.28596)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我得仔细阅读论文摘要，找出核心内容。  问题部分，摘要提到在接触丰富的操作中，不同阶段需要不同的多模态行动和快速反应。标准扩散策略使用固定频率和采样步骤，导致无法平衡多模态保留和快速响应。这里的关键是固定频率带来的折中问题。  方法部分，FA-RDP的创新点有两个：一是共享的多频Transformer预测不同频率的动作片段，二是动态选择采样频率，用多模态指示器在接触前用低频多步采样，接触后用高频单步。另外还有MCD，重新参数化扩散网络，保留监督。需要突出这些创新点，避免技术细节。  结论部分，实验显示FA-RDP在三个任务中成功率最高，同时保留接触前的多模态轨迹。要强调成果。  现在要确保问题、方法、结论各部分简洁，不换行，总字数不超过300。检查是否有冗余，比如“contact-rich manipulation”可以简化为“接触丰富操作”。确认核心创新点已突出，如频率自适应、动态选择、多频Transformer、MCD。最后按格式输出，确保同一行，无换行符。 </think> 问题：接触丰富操作中标准扩散策略固定频率采样导致多模态保留与快速响应难以平衡；方法：FA-RDP通过共享多频Transformer动态切换低频多步采样（接触前）与高频单步采样（接触后），引入多模态指示器与Manifold Consistency Distillation优化网络参数；结论：FA-RDP在三个任务中成功率达最高并有效保留接触前多模态轨迹。|
|**2026-07-29**|**Failure Detection for Surgical Robot Imitation Policies via Flow-Matching World Modeling**|Zhefeng Huang et.al.|[2607.27511](http://arxiv.org/abs/2607.27511)|null|摘要生成失败：429 Client Error: Too Many Requests for url: https://open.bigmodel.cn/api/paas/v4/chat/completions|
|**2026-07-28**|**MoMo: Dial Motion Mode in Robot Manipulation with Spatiotemporal Action Tokenization**|Yuhan Hu et.al.|[2607.26315](http://arxiv.org/abs/2607.26315)|null|<think> 嗯，用户让我用中文精简总结这篇论文，按照【问题】【方法】【结论】的格式，控制在300字以内，还要突出核心创新点，避免技术细节。首先，我需要仔细阅读论文摘要，抓住关键点。  论文的问题是关于机器人如何在不同环境中调整动作模式，是否可以将这些动作模式作为可复用的行为因素。方法部分提到了MoMo框架，分为两个阶段：时空动作分词器和行为克隆Transformer，输入任务和连续运动模式条件。结论显示，MoMo在不同任务中能动态调整动作模式，成功迁移到未见过的情况，证明动作模式可复用。  用户要求直接输出总结，不换行，不包含其他解释。需要注意格式严格，所有内容在同一行，用【】括起来。要突出创新点，比如动作模式作为共享因素，两阶段框架，动态调整和迁移。技术细节比如具体任务数量或评估指标可能需要省略，保持简洁。检查字数，确保不超过300字。最后，确保没有使用Markdown，正确使用中文标点，避免错误。 </think> 【问题】机器人需根据任务、物体和环境动态调整动作模式，能否将其抽象为可复用的行为因素【方法】提出MoMo框架，通过时空动作分词器提取动态行为特征，结合行为克隆Transformer以任务和连续运动模式条件驱动自适应动作生成【结论】实验验证动态模式可跨任务迁移，实现未见过任务-模式组合的稳定控制与成功执行，证明运动模式作为通用行为要素的有效性。|
|**2026-07-28**|**S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information**|Kaneyoshi Hiratsuka et.al.|[2607.26047](http://arxiv.org/abs/2607.26047)|null|<think> 好的，我现在需要处理用户的这个请求。首先，用户希望我精简总结一篇论文，按照【问题】【方法】【结论】的格式，控制在300字以内，并且要突出核心创新点，避免技术细节。用户还特别强调要严格按照格式输出，所有内容在同一行内，不能有换行符或其他解释。  首先，我需要仔细阅读用户提供的论文信息。论文标题是S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information。摘要里提到，声音信息能提供物体位置、材质和接触运动变化的信息，提出了新的听觉感知操作任务，让机器人通过听觉线索确定操作目标，需要声音源定位和识别来主动探索操作。然后他们提出了一个多模态模仿学习框架S2A2，整合视觉特征和声学空间、信号信息。他们整合了ACT、Diffusion Policy等策略到框架中，仿真实验证明在需要位置和音色任务中最有效，真实机器人实验验证了适用性。  接下来，我需要按照用户的要求来总结。问题部分应该说明研究的目标或挑战，即机器人如何利用听觉信息进行操作任务。方法部分要突出核心创新点，即S2A2框架整合视觉和声学空间/信号信息，并整合多种策略。结论部分则是仿真和真实实验都验证了有效性。  需要注意的是，用户要求避免技术细节，所以不能提到具体的策略名称如ACT、Diffusion Policy等，但可能需要提到整合了多种策略。同时要确保总字数在300以内，并且严格按照格式，同一行输出，没有换行符。  现在检查是否符合所有要求：问题、方法、结论各部分是否准确，是否突出创新点，是否有不必要的细节。可能的问题点在于是否要提到“主动探索”或者“真实机器人实验”，但用户要求避免技术细节，所以可能需要简化。例如，结论部分可以简化为“仿真与实机实验验证有效性”。  最后，确保语言精简，没有冗余，并且严格按照格式。可能需要多次调整措辞，确保符合字数限制。例如：  问题：机器人如何利用听觉线索确定操作目标，需声音源定位与识别 方法：提出S2A2框架整合视觉与声学空间/信号信息，集成多策略 结论：仿真与实机实验验证其在位置与音色任务中的有效性  检查字数|
|**2026-07-28**|**Tri-Manual Visuomotor Imitation Learning of Robot Policies**|James Zhao et.al.|[2607.25731](http://arxiv.org/abs/2607.25731)|null|<think> 好的，我需要帮用户总结这篇论文。首先，用户要求用中文精简总结，严格按照【问题】【方法】，总字数控制在300字以内。用户还强调要突出核心创新点，避免技术细节，直接输出总结，格式必须严格，同一行内，不要换行或其他解释。  先看论文标题和摘要。问题在于三手动操作中，单个人只能同时控制两个手臂，导致传统双手动操作的方法不适用。传统方法假设操作者与机器人的控制通道数量匹配，但三手动系统需要同时协调三个手臂，而人只能控制两个，因此可能存在模式切换的问题，导致行为克隆出现延迟，而不是任务本身需要的延迟。  方法部分，论文提出了TriManPolicy系统，核心是Dependency-Aware Tri-Arm Scheduling（DATS）。关键点在于重新调整演示数据的顺序，保持局部传感器运动段，根据任务顺序和手臂使用限制进行重新排列，训练一个同步策略。用户强调要突出创新点，所以需要强调 DATS 的核心机制，即保留局部段并重新调度，而部署时不需要依赖图或调度器。  结论部分，在六个实际任务中，使用DATS调整后的演示数据训练的策略在协调效率上更优，任务成功率相当，同时 offline 分析显示监督方式变化而非仅仅去除空闲期。  现在需要将这些信息浓缩成问题、方法、结论三个部分，每部分用中文，不超过300字，同一行，无换行。要注意避免技术细节，比如具体的六个任务类型不需要提，重点在创新点和结果。  检查格式是否正确，确保没有换行，所有内容在同一行。例如：  【问题】三手动操作中单操作者无法同步控制三臂，传统行为克隆导致界面延迟而非任务延迟；【方法】TriManPolicy通过Dependency-Aware Tri-Arm Scheduling（DATS）重新调度演示数据，保留局部运动段并按任务约束调整顺序；【结论】在六项任务中，DATS训练的同步策略提升协调效率且任务成功率相当，offline分析显示监督方式变化而非仅去除空闲期。  确认字数是否符合，核心创新点是否突出，技术细节是否被省略。例如，“DATS”需要解释为重新调度演示数据，保留局部段，按约束调整顺序，而结论部分强调结果和核心发现。 </think> 【问题】三手动操作中|
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

