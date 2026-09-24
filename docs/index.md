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

## Updated on 2026.09.24
> Usage instructions: [here](./docs/README.md#usage)

## Reinforcement Learning

| Publish Date | Title | Authors | PDF | Code | 摘要 |
|:---------|:-----------------------|:---------|:------|:------|:-------------------------------------|
|**2026-09-22**|**ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model**|Sinuo Wang et.al.|[2609.26299](http://arxiv.org/abs/2609.26299)|null|<think> 好的，用户让我总结一篇论文，按照【问题】【方法】，总字数控制在300字以内，还要突出核心创新点，避免技术细节。首先，我需要仔细阅读论文的摘要，找出关键点。  论文的问题在于现有的潜在世界模型虽然能预测未来，但不够适用于自动驾驶规划。预测结果通常用于预训练或辅助监督，而不是直接指导轨迹生成。方法部分提到了ForeDrive，学习与规划相关的潜在表示，并耦合到Diffusion Transformer（DiT）规划器中。规划器使用多时间步的潜在未来表示，通过JEPA式世界模型学习。梯度更新共享编码器，而停止梯度路由训练潜在预测器。此外，还有视觉融合、未来状态注入和TAB技术来处理不同可靠性和BEV与图像的不对齐问题。训练使用纯模仿学习，只用前视图像，效果不错。  用户要求精简总结，严格按照格式，不换行，不解释。我需要确保问题和方法部分准确，突出创新点，比如不对称耦合、多时间步预测、视觉融合和TAB。同时注意字数限制，可能需要合并句子，比如将方法中的多个技术点用逗号分隔。检查是否符合所有要求，比如格式、字数、不包含技术细节。最后确保输出正确，没有换行或多余内容。 </think> 【问题】现有潜在世界模型优化未来预测性但缺乏规划适用性，预测结果未直接用于轨迹生成；自动驾驶需多时间步未来信息且存在BEV与图像对齐问题【方法】ForeDrive通过不对称耦合规划相关潜在表示与DiT规划器，利用JEPA式模型学习多时间步潜在未来，规划梯度更新共享编码器而停止梯度路由训练预测器，结合未来状态注入、 gated视觉融合和Trajectory-Adaptive Bias解决预测可靠性与模态对齐问题，纯模仿学习训练仅用前视图像生成轨迹【结论】在NAVSIM数据集上达到89.9-90.0 PDMS/EPDMS，无需强化学习或外部轨迹评分器|
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
|**2026-09-23**|**AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios**|Zhipeng Bao et.al.|[2609.28366](http://arxiv.org/abs/2609.28366)|null|<think> 好的，我现在需要帮用户精简总结这篇论文，按照指定的格式，控制在300字以内。首先，我得仔细阅读用户提供的论文摘要，抓住核心问题和方法，然后提炼结论。  论文标题是AnchorReasoning，主要针对长尾自动驾驶场景中的视觉语言模型（VLMs）的问题。问题部分应该提到现有数据集在连接视觉证据与推理和规划上的不足，导致监督不足。方法部分要突出他们构建的AnchorReasoning数据集，包含大量标注帧和决策关键元素，以及VG-CoT链条和课程学习策略，还有评估指标。结论部分则是实验结果，比如ADE和FDE的下降，RFS的提升，以及效率上的优势。  用户要求突出核心创新点，避免技术细节。所以我要确保问题、方法、结论都简洁，不涉及太多技术术语。比如，VG-CoT可能不需要详细解释，只要说明是视觉化的推理链条。课程学习策略可以简化为“渐进式课程学习”。  还要注意格式，严格按照【问题】【方法】，总字数限制。可能需要多次精简，比如把“包含416,119 annotated frames”简化为“超41万帧标注数据”，同时保留关键数字。另外，用户强调不要换行符，所有内容在同一行，所以需要检查格式是否符合。  最后检查是否符合字数要求，确保不超过300字。可能还需要调整语句结构，使其更紧凑。例如，将实验结果中的具体数字整合到结论中，同时保持流畅。确认没有遗漏核心创新点，如决策关键元素、VG-CoT、课程学习和评估指标。 </think> 【问题】长尾自动驾驶场景中视觉语言模型缺乏连接决策关键视觉证据与推理规划的监督数据，导致决策质量与规划能力不足；【方法】构建含416,119帧、395,379决策关键元素的AnchorReasoning数据集，设计视觉化推理链条（VG-CoT）与渐进式课程学习策略，开发物体尺寸感知的定位评估指标；【结论】实验表明VG-CoT监督使8种模型ADE/FDE降低7.84/11.86，RFS提升1.66/1.70，推理token减少18.5个且推理速度提升0.32s/帧，验证决策导向的视觉化监督对长尾自动驾驶规划的有效性。|
|**2026-09-23**|**Distillation for Efficient Multitask Manipulation Policies via Conditional Flow Matching**|Shreya Deshmukh et.al.|[2609.28107](http://arxiv.org/abs/2609.28107)|null|<think> 好的，我现在需要处理用户的请求，帮他精简总结一篇论文。首先，我得仔细阅读用户提供的资料，确保理解每个部分的要求。用户给了一个论文的标题和摘要，要求按照【问题】【方法】，总字数控制在300字以内，突出核心创新点，避免技术细节，严格按照格式输出，同一行内，不要换行，不带其他解释。  首先，我需要解析论文的问题和方法。问题部分应该说明研究中的挑战，比如多任务政策学习中的计算成本和性能下降。方法部分要突出他们的创新点，也就是知识蒸馏和共享政策，结合条件流匹配和蒸馏信号。结论部分则是实验结果，在RLBench上表现更好且模型大小固定。  接下来要注意用户强调的格式，必须严格按照【问题】【方法】，总字数限制。用户可能希望快速获取论文的核心内容，不需要详细的技术细节，所以需要提炼关键点。同时，用户要求所有内容在同一行，不能换行，这可能需要仔细控制字数，确保不超过限制。  然后，我需要检查是否有遗漏的核心创新点。论文中提到的问题是多任务训练的困难和现有方法的不足，方法是用蒸馏将单任务专家的知识转移到多任务共享政策，结合原始CFM目标。结论是实验验证了有效性。这些都需要准确表达。  还要注意避免技术术语过多，比如“velocity fields”可以简化为“知识”或“条件流匹配模型”。同时，确保语言简洁，符合中文表达习惯。可能需要多次调整，确保字数符合要求，同时信息完整。  最后，检查格式是否正确，没有换行，没有多余的解释，严格按照用户提供的模板。可能需要多次精简，比如将“通过条件流匹配训练的单任务专家”简化为“单任务CFM专家”，确保每个部分的信息准确且简洁。  总结下来，我需要将问题、方法、结论三个部分分别提炼，确保核心创新点突出，语言精炼，符合格式和字数要求。现在可以开始撰写最终答案了。 </think> 【问题】多任务政策学习存在计算成本高、性能下降问题；【方法】通过蒸馏将单任务CFM专家的条件流匹配知识迁移至共享多任务政策，结合原始CFM目标；【结论】在RLBench上实现性能提升且模型规模固定。|
|**2026-09-22**|**Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation**|Hao Wei et.al.|[2609.26672](http://arxiv.org/abs/2609.26672)|null|<think> 嗯，用户让我总结这篇论文，要求按照【问题】【方法】【结论】的格式，控制在300字以内，还要突出核心创新点，避免技术细节。首先，我需要仔细阅读论文的摘要，找出关键点。  问题部分，论文提到训练高精度机器人操作模型需要大量特定任务的高质量数据，收集成本高且耗时。方法部分，他们提出了ε4P方法，利用两个废弃的数据源：低精度目标任务数据和错配任务的高精度数据。核心创新是控制数据在流匹配轨迹中的噪声水平，低精度数据在高噪声下保留任务上下文，高精度数据在低噪声下传递动作精度。结论部分，实验显示ε4P能提升政策性能31.7%，替换等量高质量数据时性能仅下降4.2%，证明高效利用异构数据可行。  接下来要检查是否符合格式要求，所有内容在同一行，没有换行符，不包含其他解释。需要精简语言，确保字数在300以内。可能需要调整用词，比如“流匹配轨迹”可以简化为“动态调整数据噪声水平”。同时要突出创新点，比如“动态整合低/高精度数据”和“噪声控制策略”这些关键词。最后确认是否符合用户的所有要求，特别是格式和字数限制。 </think> 【问题】训练高精度机器人操作模型依赖昂贵耗时的高质量任务数据【方法】ε4P方法动态整合低精度目标任务数据与高精度错配任务数据，通过噪声控制策略在流匹配轨迹中分别以高噪声保留任务上下文和低噪声传递动作精度【结论】实验表明该方法提升政策性能31.7%，且用等量低质量数据替代高质量数据仅降4.2%，验证了异构数据系统性复用的可行性。|
|**2026-09-22**|**ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model**|Sinuo Wang et.al.|[2609.26299](http://arxiv.org/abs/2609.26299)|null|<think> 好的，我现在需要帮用户总结这篇论文的摘要，按照他们给的格式：问题、方法、结论，控制在300字以内，还要突出核心创新点，避免技术细节。首先，我得仔细阅读用户提供的摘要内容，找出关键点。  论文标题是ForeDrive，主要解决的问题是现有的潜在世界模型虽然优化了未来预测能力，但生成的表示对自动驾驶规划并不实用。问题部分应该简洁说明这点，比如现有模型优化未来预测但无法有效用于规划。  接下来是方法部分，用户提到ForeDrive的创新点包括学习与规划相关的潜在表示，并耦合到Diffusion Transformer（DiT）规划器。这里需要突出不对称耦合、JEPA式模型、梯度更新机制以及视觉融合技术。要注意避免技术细节，比如具体的技术名称如JEPA-style可能需要简化，但用户给的例子中保留了，所以可能需要保留。另外，提到的三个技术：gated visual fusion、future-status injection、TAB，这些是核心创新点，必须包含。  结论部分需要说明结果，比如在NAVSIM上的PDMS和EPDMS成绩，以及训练方法（纯模仿学习，仅使用前视图像）。用户给的例子中直接写了这些数据，所以需要准确复制。  然后要检查是否符合格式要求：所有内容在同一行，没有换行符，严格按照问题、方法、结论的顺序。字数方面，用户给的例子是大约200字左右，所以需要精简，确保不超过300字。  现在要组织语言，确保每个部分简洁。问题部分要简明指出现有模型的不足。方法部分列出核心创新点，用分号分隔。结论部分包括结果和训练条件。需要注意术语的准确性和简洁性，比如“规划相关”的潜在表示，不对称耦合，多时间尺度潜在未来表示，梯度更新和stop-gradient路由，以及三个视觉融合技术。最后的结果数据要准确无误。  最后检查是否有技术细节过多，比如Diffusion Transformer的全称可能不需要，但用户例子中用了DiT，所以保留缩写。确保不使用换行符，所有内容紧凑排列。确认字数，确保符合要求。 </think> 问题：现有潜在世界模型优化未来预测但无法有效用于自动驾驶规划；方法：ForeDrive通过规划相关潜在表示与DiT规划器不对称耦合，采用JEPA式多时间尺度预测、梯度分离训练、gated视觉融合及TAB技术注入|
|**2026-09-22**|**History-Conditioned Flow Matching for Probabilistic Dynamics of Tendon-Driven Continuum Robots**|Hang Yang et.al.|[2609.25658](http://arxiv.org/abs/2609.25658)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我得仔细阅读用户提供的论文摘要，抓住核心内容。  问题部分应该包括研究的挑战，也就是 tendon-driven continuum robots 的确定性动力学建模困难，原因包括材料行为、传动系统、摩擦和接触不确定性。用户提到现有的关节配置和名义拉力命令无法完全表征这些内部因素，导致后续运动的不确定性。这部分需要简洁表达，突出核心问题。  方法部分要强调提出的框架，即 history-conditioned（历史条件）和 physics-informed flow-matching（物理信息流匹配）。用户提到使用运动和拉力历史预测下一个完整关节配置的分布，通过递归采样预测未来整体运动。需要指出这是针对不确定性的概率动力学预测方法，并对比了基线模型，比如条件变分自编码器和扩散模型，说明其优势。还要提到消融实验支持历史和结构条件的影响。  结论部分需要总结实验结果，包括仿真和物理机器人测试的结果，Energy Scores 的数值，预测与测量的比率，以及基线对比。要突出在两种场景下 Flow 框架的表现优于其他方法，验证了其有效性和鲁棒性。  需要注意用户要求避免技术细节，直接输出总结，严格按照格式，同一行内，无换行符，不包含其他解释。同时要突出核心创新点，比如历史条件和物理信息结合的概率预测方法，以及实际应用中的表现。  现在检查字数，确保不超过300字。可能需要调整用词，比如“通过递归采样”可以简化为“递归采样”，“消融实验”改为“消融分析”等。确保每个部分的关键词准确，比如“Energy Scores”翻译为“能量评分”，“预测-测量比”等。  最后，整合所有内容，确保格式正确，没有多余符号或换行，符合用户的具体要求。 </think> 问题：确定性建模面临材料行为、传动、摩擦和接触不确定性，历史与名义指令无法表征内部机械因素导致运动预测偏差；方法：提出基于历史条件与物理信息的流匹配框架，通过递归采样预测未来关节配置分布，结合物理约束与历史轨迹优化概率动力学模型；结论：仿真测试中能量评分优于条件VAE和扩散基线，物理机器人实验验证未知指令下预测精度（11.91/11|
|**2026-09-22**|**MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence**|Haoran Wen et.al.|[2609.25627](http://arxiv.org/abs/2609.25627)|null|<think> 好的，我现在需要帮用户精简总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，并且突出核心创新点，避免技术细节。同时，输出格式必须严格按照指定，不能有换行符或其他解释。  首先，我需要仔细阅读论文的摘要，理解其核心内容。论文的问题是关于机器人控制中模型需要理解任务意图、识别交互位置、捕捉场景动态并生成精确动作的挑战。现有的方法要么缺乏场景动态建模，要么没有明确展示任务相关的语义和空间结构。  接下来是方法部分，用户提到要突出核心创新点，所以需要提炼关键点。论文提出ME-U0模型，通过Mixture-of-Transformers架构连接理解和生成专家。这里的关键点包括多模态动态输入（RGB、深度、法线、光流）、多速率旋转位置编码（MRPE）、基于流匹配的任务预测和功能接地，以及预训练数据集的使用。此外，还要提到其在仿真和真实世界中的表现，以及零样本能力。  现在需要将问题和方法浓缩成两行，每行不超过300字。问题部分要简明扼要，说明现有模型的不足。方法部分要突出架构创新、多模态动态输入、MRPE、流匹配和预训练成果。同时注意避免技术细节，比如具体的训练数据时间（4,200小时）可能可以省略，但用户摘要中提到的是“curated demonstrations”和“egocentric datasets”，可能需要保留关键数据集名称，但用户可能希望更简洁，所以可能只保留“多模态仿真与真实数据预训练”。  最后检查是否符合格式要求，确保没有换行符，所有内容在同一行，并且字数控制在300字以内。可能需要多次调整，确保信息准确且符合用户要求。 </think> 【问题】机器人控制需同时理解任务意图、捕捉动态场景并生成精确动作，现有模型或缺乏动态建模或无法提供细粒度语义空间结构【方法】提出ME-U0统一模型，通过多模态动态输入（RGB/深度/法线/光流）与多速率旋转编码对齐视觉动态，结合流匹配实现任务预测与功能接地，基于4,200小时多模态数据预训练，在仿真与真实场景中均达到高控制成功率并具备零样本迁移能力【结论|
|**2026-09-22**|**From Instrument-Mounted Demonstrations to In-Vivo Execution: Learning Bimanual Laparoscopic Appendectomy Without Robot-Collected Demonstrations**|Dongho Yee et.al.|[2609.25625](http://arxiv.org/abs/2609.25625)|null|<think> 好的，我现在需要帮用户精简总结这篇论文，按照指定的格式来。首先，用户的要求很明确，要控制在300字以内，严格按照【问题】【方法】，总字数要少，而且不能有换行符。  首先看问题部分。论文的摘要里提到，微创手术通常用手持器械，但手术结束后器械的运动学数据丢失，只有内窥镜视频保留。所以问题应该是缺乏可用的器械运动数据用于训练机器人。需要简练地表达这一点，比如“微创手术器械运动数据在术中丢失，依赖内窥镜视频无法训练机器人”。  接下来是方法部分。论文的核心创新点有几个：他们开发了一个器械状态记录器，用惯性传感器、飞行时间传感器和霍尔传感器，不需要外部摄像头或追踪器。然后他们有一个数据管道处理传感器延迟，对齐数据形成观测-动作对。接着用物理模拟器重构环境，训练扩散政策，调整DINOv3模型。之后在活体动物上收集849个真实演示数据，训练并部署机器人，由外科医生选择手术阶段，机器人只做执行和校准。  需要把这些步骤提炼出来，突出创新点，比如“开发无外部视觉的器械状态记录器，多传感器数据对齐与物理仿真辅助政策训练，活体数据迭代优化”。避免技术细节，比如具体的传感器类型可能不需要全写，但用户可能希望保留关键传感器组合，所以可能需要提到惯性、飞行时间和霍尔传感器。  结论部分，论文的结论是他们的方法有效，机器人能完成手术，且演示数据来自真实器械足够，机器人仅作参考和执行。需要总结为“证明真实器械演示可训练机器人完成活体手术，机器人仅作执行与校准”。  现在检查字数，确保每部分不超过限制。问题、方法、结论各部分要简洁，用分号分隔，所有内容在同一行，无换行符。可能需要调整用词，比如“活体数据迭代优化”是否准确，或者是否有更合适的表达。确保核心创新点突出，比如无外部视觉、多传感器融合、物理仿真辅助、活体数据迭代等。  最后，确保格式正确，没有多余的解释，严格按照用户给的模板。可能还需要检查是否有重复或冗余的信息，比如“数据管道”可以简化为“数据对齐”，而物理模拟器部分可能简化为“物理仿真辅助”。最终整合|
|**2026-09-22**|**RoboMP-DINOv2: Prompts, Not Filters for Robust Robot Manipulation**|Han Qi et.al.|[2609.25506](http://arxiv.org/abs/2609.25506)|null|<think> 好的，我需要帮用户总结这篇论文，按照要求的格式，分问题、方法、结论三部分，控制在300字以内，突出核心创新点，避免技术细节。首先，我得仔细阅读论文摘要，抓住关键点。  论文标题是RoboMP-DINOv2，核心问题应该是机器人抓取在视觉变化和场景干扰下的泛化能力不足，现有方法用分割掩码作为硬过滤器，可能丢失有用信息。方法部分，他们提出用mask作为prompt而不是filter，这样可以在全场景中提取密集特征，同时注入区域特定的嵌入，结合prompt和未prompt的token进行预测。还引入了MCR来增强颜色鲁棒性。结论部分，实验显示他们的方法在多个模拟环境中表现更好，尤其是在颜色变化和场景杂乱的情况下，成功率显著提高，同时保留了关键行为信息。  现在需要将这些内容精简，确保每个部分简洁，不超过字数限制。检查是否有技术细节需要省略，比如具体的模型结构或训练细节。确保问题、方法、结论各部分清晰，核心创新点突出，比如mask作为prompt而不是filter，以及MCR的引入。最后，确认格式正确，同一行，无换行，无其他解释。 </think> 问题：机器人抓取需在视觉变化和场景干扰下泛化，现有方法用分割掩码作为硬过滤器导致有用信息丢失。方法：提出RoboMP-DINOv2将mask作为空间prompt而非过滤器，从全场景提取密集特征，注入区域嵌入并联合上下文化prompt和未prompt token进行预测，引入 masked-region color randomization (MCR) 提升颜色鲁棒性。结论：实验表明RoboMP-DINOv2在视觉偏移和场景杂乱下成功率60.7%和59.7%优于DINOv2基线，MCR在未现颜色下达72.5%成功，同时保留行为相关信息。|
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

