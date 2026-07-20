## Updated on 2026.07.20
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
|**2026-07-17**|**Data and Learning Where it Matters for Contact-Rich Manipulation**|Oliver Hausdörfer et.al.|[2607.15982](http://arxiv.org/abs/2607.15982)|null|<think> 好的，我现在需要帮用户总结这篇论文。首先，用户的要求很明确，要用中文精简总结，严格按照问题、方法、结论的格式，控制在300字以内。而且要突出核心创新点，避免技术细节，直接输出，不能换行，也不能有其他解释。  先看论文标题和数据。标题是“Data and Learning Where it Matters for Contact-Rich Manipulation”，摘要里提到传统端到端学习在精度高和泛化任务中表现脆，问题出在数据收集缺乏结构和重点。他们的方法是在关键接触任务用密集数据，简单任务用传统规划，结合自动化数据收集和离线强化学习，不需要远程操作员和在线更新。结果在四个任务中用2-2.5小时数据，成功率96%，远超基线55%，且在OOD场景表现好。  接下来需要提炼问题、方法和结论。问题部分要说明传统方法的问题，即数据收集不聚焦导致脆和泛化差。方法部分要突出关键任务密集数据，简单任务传统规划，自动化数据收集和离线RL。结论是高成功率，OOD表现好，为精准应用和数据收集提供方向。  需要注意用户强调的核心创新点，所以问题部分要明确数据收集的结构和重点缺失，方法部分自动化数据收集和离线RL的结合，结论部分成功率和OOD优势。同时要避免技术细节，比如具体的算法名称可能不需要提，但离线强化学习是关键。  然后检查字数，确保每部分简洁。问题部分大概30字，方法50字，结论50字，总在300以内。还要确保同一行，不换行，用空格分隔。可能需要调整用词，比如“自动化数据采集”代替“自动化数据收集”，更简洁。  最后确认是否符合格式要求，没有换行，没有多余解释，核心创新点突出。比如问题部分明确数据结构缺失，方法部分关键任务和简单任务的分工，结论的高成功率对比和OOD表现。这样应该满足用户需求了。 </think> 问题：传统端到端学习在接触密集型高精度任务中数据收集缺乏结构导致脆化和泛化不足；方法：针对关键接触任务进行自动化密集数据采集结合离线强化学习，简单任务采用传统规划，消除远程操作员依赖和在线更新；结论：2-2.5小时自主数据即可达96%成功率，远超基线|
|**2026-07-16**|**WorkDrive: Roadwork Chain of Causation for Autonomous Driving**|Tianyi Jiang et.al.|[2607.14727](http://arxiv.org/abs/2607.14727)|null|<think> 好的，我现在需要帮用户精简总结这篇论文，按照指定的格式来。首先，我得仔细阅读用户提供的论文摘要，理解核心内容。论文的问题是关于自动驾驶中的VLM在道路施工区域的表现不佳，因为熟悉的光学线索被改变或消失，临时设施重新定义了行驶区域。现有的模型虽然能检测这些物体，但没有明确的指导，导致推理错误。  接下来是方法部分，用户提到WorkDrive框架，构建感知驱动的因果推理，并与其他方法结合。需要突出自动化多任务感知管道和因果推理注释流程，以及后续的强化学习。结论部分要说明在ROADWork数据集上的效果提升，特别是ADE和GRPO的改进。  用户要求避免技术细节，直接输出总结，严格按照格式，同一行内，无换行。核心创新点应该是因果推理框架和奖励机制。需要检查字数是否在300字以内，确保问题、方法、结论各部分简洁。可能需要注意术语的准确，比如“Chain-of-Causation”要翻译正确，保持一致性。最后确认是否符合所有格式要求，没有多余的解释或换行。 </think> 问题：自动驾驶视觉语言模型在道路施工区域存在推理偏差，依赖预训练熟悉元素而忽略临时设施导致的规划错误；方法：提出WorkDrive框架，通过自动化多任务感知管道提取施工区域结构化事实并注入因果推理注释流程，结合强化学习以轨迹侧移元动作与预测轨迹一致性为单一奖励进行优化；结论：在ROADWork数据集上使轨迹平均偏移误差降低9.0%和3.0%，优于纯轨迹基准。|
|**2026-07-13**|**Robust In-Hand Manipulation via Priors in Reinforcement Learning and Mechanical Design**|Yifei Chen et.al.|[2607.12105](http://arxiv.org/abs/2607.12105)|null|<think> 好的，我现在需要帮用户精简总结这篇论文，按照指定的格式来。首先，我得仔细阅读用户提供的论文摘要，理解核心内容。  论文的问题是关于在无外部感知的情况下进行手部抓握的挑战，主要来自指尖与物体的接触不确定性和重力干扰。现有的强化学习方法虽然能学习复杂的指尖动作，但没有优先考虑保持良好的抓握状态以持续操作。用户要求突出核心创新点，避免技术细节，所以我要抓住这两个关键点：全局抓握质量和局部接触几何的先验。  接下来是方法部分，论文提出了两个互补的物理先验。一个是全局的抓握质量先验，基于经典抓握分析，作为密集的奖励塑造项，鼓励接触分布良好且抗力矩能力强的抓握。另一个是局部的接触几何先验，基于指尖曲率，机械上调整接触界面，促进任务对齐的滚动并减少侧向漂移。需要确保这两个点清晰，但不用深入技术细节。  结论部分，实验结果显示这些先验在旋转效率、抓握稳定性和抗干扰方面有显著提升，说明在学习和指尖形态中嵌入物理先验能提高任务鲁棒性和虚实迁移。用户强调要控制在300字以内，所以必须简洁。  现在要检查格式是否符合要求：问题、方法、结论，每部分用【】括起，所有内容同一行，无换行符。需要确保不遗漏核心创新点，比如“两个互补的物理先验”和“全局与局部结合”，同时避免技术术语如“奖励塑造项”等细节。最后确认字数，确保不超过限制。可能用户是研究者或学生，需要快速了解论文贡献，所以重点突出创新和结果，而非方法的具体实现。可能还需要注意术语的准确性和简洁性，确保专业读者能一目了然。 </think> 【问题】在无外部感知的手持抓握中，指尖接触不确定性和重力干扰导致抓握稳定性差，现有强化学习未优先维持优质抓握以支撑持续操作【方法】提出全局抓握质量先验（基于经典分析优化接触分布与抗力矩）和局部接触几何先验（通过指尖曲率调整接触界面促进对齐滚动）两大互补物理先验【结论】实验表明融合先验的强化学习显著提升旋转效率、抓握稳定性和抗干扰能力，物理先验嵌入学习与指尖形态设计|
|**2026-07-13**|**A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation**|Yunhai Feng et.al.|[2607.11874](http://arxiv.org/abs/2607.11874)|null|<think> 好的，我现在需要帮用户精简总结这篇论文。首先，用户的要求很明确，要严格按照问题、方法、结论的格式，控制在300字以内，突出核心创新点，避免技术细节。  先看论文标题和摘要。标题提到的是最小化的重定向引导强化学习食谱，应用于灵巧抓取。摘要里说之前的人形机器人全身控制成功的方法是将人类动作重定向到机器人运动学参考，然后用强化学习训练策略跟踪。但灵巧抓取不同，因为涉及复杂接触动力学和接触模式调节。作者提出了REGRIND，一个简化的流程，从单一人类示范学习抓取策略。重定向时保持手-物体空间和接触关系，在仿真中训练残差RL策略跟踪物体中心关键点，然后零样本迁移到硬件，通过系统识别。实验显示在剪刀和螺丝刀任务中表现流畅，并分析了虚实迁移的关键因素，提供指导。  现在需要提炼问题、方法和结论。问题部分要说明灵巧抓取的挑战，即复杂接触动力学和接触模式调节，以及如何迁移策略。方法部分要突出REGRIND的核心步骤：重定向保持手-物关系，仿真训练残差RL策略，零样本迁移和系统识别。结论是策略有效，分析了虚实迁移的关键因素，提供指导。  要注意避免技术细节，比如具体如何重定向，残差RL的具体结构等。要确保每个部分简洁，不超过字数限制。检查格式是否正确，所有内容在同一行，没有换行，符合用户的要求。 </think> 问题：灵巧抓取需解决复杂接触动力学与接触模式调节，传统重定向RL难以有效迁移策略；方法：REGRIND通过重定向保持手-物空间关系，仿真训练物体中心关键点残差RL策略，零样本迁移结合系统识别；结论：实现多手工具任务流畅人样行为，揭示虚实迁移关键因素并提供实践指导。|
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

<p align=right>(<a href=#updated-on-20260720>back to top</a>)</p>

## Imitation Learning & SFT

|Publish Date|Title|Authors|PDF|Code|摘要|
|---|---|---|---|---|---|
|**2026-07-17**|**Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation**|Zhenduo Shang et.al.|[2607.15880](http://arxiv.org/abs/2607.15880)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结一篇论文。首先，用户的要求很明确，要按照【问题】【方法】，总字数控制在300字以内，并且严格按照格式输出，不能有换行符或其他解释。我得仔细分析用户提供的论文摘要，找出核心问题和方法，同时突出创新点，避免技术细节。  首先，问题部分。论文摘要提到，现有的模仿学习主要依赖同一领域的任务，导致在未见任务上泛化能力差，存在数据稀缺和环境泛化的问题。我需要将问题简洁地表达出来，比如“机器人抓取任务中，传统模仿学习依赖单一领域数据，导致对未见任务泛化能力不足”。  接下来是方法部分。论文的核心创新点包括DAMI框架、VMT模块、U2T块和TCFM机制。需要将这些整合成简短的描述，强调元学习构建共享技能空间、捕捉动态轨迹、融合多模态数据以及通过内在动力学学习任务逻辑。同时要提到在仿真和现实中的实验验证。  需要注意用户要求避免技术细节，所以不能深入解释每个模块的具体作用，而是概括整体机制。例如，VMT模块和U2T块可以合并为“设计VMT模块捕获任务动态轨迹，U2T块融合多模态数据”，而TCFM机制可以简化为“通过TCFM机制协调特征表示”。  还要确保总字数在300字以内，所以语言必须精炼。检查是否符合格式，所有内容在同一行，没有换行符，严格按照【问题】【方法】的结构。可能需要多次调整，确保信息完整且符合要求。  最后，验证是否突出了核心创新点，比如元学习、动态轨迹、多模态融合和内在动力学学习，这些是论文的关键贡献。确认没有遗漏重要信息，同时保持简洁。完成后，再检查格式是否正确，确保用户可以直接复制使用。 </think> 【问题】机器人抓取任务中，传统模仿学习依赖单一领域数据，导致对未见任务泛化能力不足，存在数据稀缺和环境适应性差的问题；【方法】提出DAMI框架，通过元学习构建共享技能空间实现快速迁移，设计VMT模块捕获任务动态轨迹，U2T块融合多模态数据，利用TCFM机制协调3D特征，基于随机完整参考演示学习任务内在动力学而非静态记忆，在仿真与真实场景验证中显著提升直接|
|**2026-07-16**|**WorkDrive: Roadwork Chain of Causation for Autonomous Driving**|Tianyi Jiang et.al.|[2607.14727](http://arxiv.org/abs/2607.14727)|null|<think> 好的，用户让我总结一篇关于自动驾驶在施工区域处理的论文，要求严格按照问题、方法、结论的格式，控制在300字以内，突出核心创新点，避免技术细节。首先，我需要仔细阅读论文摘要，抓住关键点。  问题部分应该指出自动驾驶在施工区域的表现不佳，视觉语言模型依赖预训练中的常见元素，导致决策错误。方法部分需要强调WorkDrive框架，包括因果推理构建、多任务感知管道和注意力引导，以及后续的强化学习。结论部分要说明误差降低的数据，特别是CoC和GRPO的效果。  用户要求直接输出，不换行，不解释。我需要确保每个部分简洁，用最少的字表达清楚。比如问题部分要简明扼要，方法突出自动化管道和因果标注，结论用具体数据。还要检查字数，确保不超过限制。可能需要注意术语的准确性，比如“Chain-of-Causation”要缩写为CoC，保持一致性。最后确认格式是否正确，所有内容在同一行，没有换行符或其他多余内容。 </think> 问题：自动驾驶视觉语言模型在施工区域存在决策偏差，依赖预训练数据忽略临时路障导致规划错误；方法：WorkDrive构建因果推理框架，通过自动化感知管道提取施工特征并引导标注，强化学习优化轨迹一致性；结论：在ROADWork数据集上CoC使轨迹平均偏移降低9%，一致性强化学习再降3%，优于纯轨迹基线。|
|**2026-07-16**|**BridgeFlow: Fast and Robust SE(2)-Equivariant Motion Planning with Flow Matching**|Xinzhe Zhou et.al.|[2607.14725](http://arxiv.org/abs/2607.14725)|null|<think> 好的，我现在需要帮用户总结这篇论文，按照他们的格式要求。首先，用户希望用中文精简总结，控制在300字以内，分问题、方法、结论三个部分，每部分都要突出核心创新点，避免技术细节。  先看论文标题和摘要。标题是BridgeFlow，强调快速且鲁棒的SE(2)-等变的运动规划，使用流匹配。摘要里提到当前学习型规划器面临的问题：要么缺乏内在等变性，要么用专用架构导致实时推理瓶颈。他们提出BridgeFlow，用轻量化的任务中心归一化模块实现等变性，结合布朗桥先验和上下文感知的小批量最优传输，还有无监督指导分类器。  问题部分需要点出当前方法的不足，即缺乏等变性导致无法有效泛化，或者专用架构影响实时性。方法部分要突出他们的创新点：轻量归一化模块、布朗桥和最优传输加速，以及CFG嵌入环境意识。结论则是性能提升，速度和轨迹成功率超过基线，泛化能力强。  用户要求严格格式，所有内容在同一行，无换行，所以需要确保每个部分简洁，用分号分隔。检查字数，确保不超过300字。可能需要注意术语的准确性，比如SE(2)-equivariant翻译成SE(2)-等变，避免技术细节如“扩散基线”等，但用户允许提到比较对象。最后确认是否符合所有要求，没有多余解释，直接输出总结。 </think> 问题：当前学习型运动规划器面临等变性与实时性矛盾，缺乏空间等变导致泛化能力弱或依赖专用架构降低推理速度；方法：提出BridgeFlow框架，通过任务中心归一化模块实现严格SE(2)-等变，结合布朗桥流场加速与上下文感知最优传输，嵌入无监督环境指导；结论：在密集环境中实现15倍速度提升和2倍轨迹成功率，支持未见环境及任意空间变换的鲁棒泛化，优于扩散基线。|
|**2026-07-13**|**Mixture of Frames Policy: Multi-Frame Action Denoising for Bimanual Mobile Manipulation**|Dian Wang et.al.|[2607.11884](http://arxiv.org/abs/2607.11884)|null|<think> 好的，我现在需要帮用户总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】【结论】的格式，控制在300字以内，用中文，突出核心创新点，避免技术细节。  先看论文的摘要。问题部分提到机器人操作是多帧的，不同任务在不同坐标系下更简单，但现有的扩散模型只用一个预设的坐标系，导致模型复杂度过高。方法部分他们提出了Mixture of Frames Policy（MoF），在多个坐标系同步去噪，使用专用去噪器，并通过6D旋转表示进行变换。结论显示MoF在多个任务中优于单帧和MoE模型，且在真实场景中表现更好。  接下来要精简。问题要突出多帧需求与单帧模型的矛盾。方法要强调多帧同步去噪和旋转表示的创新。结论要说明任务依赖和性能提升。注意用户要求所有内容在同一行，无换行，所以需要用空格分隔。还要检查字数，确保不超过300字。可能需要调整用词，比如“引入6D旋转表示”而不是详细说明SE(3)参数化。确保核心创新点如多帧同步、专用去噪器、6D旋转都提到，但省略技术细节如SE(3)和SO(3)的区别。最后检查格式是否符合要求，没有多余的解释。 </think> 【问题】机器人操作需多帧协同但现有单帧扩散模型复杂度过高【方法】提出Mixture of Frames Policy通过多帧同步去噪、专用去噪器融合及6D旋转表示实现多坐标系转换【结论】在九项仿真和两项真实任务中显著优于单帧和混合专家模型，且最佳帧选择依赖任务特性。|
|**2026-07-13**|**Pix2Act: Image-Space Manipulation Policies with Equivariant Augmentation**|Haojie Huang et.al.|[2607.11167](http://arxiv.org/abs/2607.11167)|null|<think> 好的，我现在需要处理用户的查询，帮他总结一篇论文。首先，我得仔细阅读用户的要求，确保完全理解。用户希望用中文精简总结，严格按照【问题】【方法】，总字数控制在300字以内。还要突出核心创新点，避免技术细节，直接输出总结，格式严格，同一行内，不要换行符和其他解释。  首先，我需要解析论文的摘要。论文标题是Pix2Act: Image-Space Manipulation Policies with Equivariant Augmentation。摘要中提到，将操作动作表示为相机平面中的2D轨迹，虽然紧凑且可解释，但存在相机外轨迹和精度限制的问题。他们提出的方法是生成连续的图像空间关键点轨迹，并通过三角测量无损失地恢复末端执行器姿态，将三维控制问题转化为更简单的二维预测问题。核心创新点在于使用同坐标空间对齐观察和动作，允许通过equivariant变换旋转单个相机图像及其动作，分析对称性并设计网络架构融合多视角同时尊重各视角旋转，从而扩大数据分布支持，学习不变动作结构，提升泛化性和性能。  接下来，用户要求的问题和方法部分需要突出核心创新点，避免技术细节。问题部分应简明指出挑战：图像空间轨迹的相机外和精度问题，导致三维控制复杂。方法部分需要总结Pix2Act如何解决，即生成图像空间轨迹，同坐标空间对齐，equivariant变换，对称性分析和多视角网络架构，从而提升泛化。  需要注意用户强调严格按照格式，同一行内，无换行符。所以需要将问题、方法、结论各部分用【】括起，用中文，总字数控制在300字以内。结论部分在用户提供的例子中没有出现，但根据摘要，结论应该是Pix2Act在模拟和真实任务中优于基线，鲁棒于相机扰动。但用户给的例子输出中没有结论部分，可能用户漏了，但根据要求，用户提供的示例输出中确实有结论部分，所以需要包含。  检查用户提供的示例输出，发现确实有结论部分。所以需要确保总结包含问题、方法、结论三个部分。但用户现在的查询中，示例输出中的结构是【问题】【方法】【结论】，但用户当前的查询中的示例输出可能没有，需要确认。根据当前用户的查询，用户提供的示例输出是：  【问题】三维控制复杂度高且易受相机|
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

<p align=right>(<a href=#updated-on-20260720>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/HuJiaming11/rl-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/HuJiaming11/rl-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/HuJiaming11/rl-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/HuJiaming11/rl-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/HuJiaming11/rl-arxiv-daily/issues

