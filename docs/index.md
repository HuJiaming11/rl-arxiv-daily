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

## Updated on 2026.07.11
> Usage instructions: [here](./docs/README.md#usage)

## Reinforcement Learning

| Publish Date | Title | Authors | PDF | Code | 摘要 |
|:---------|:-----------------------|:---------|:------|:------|:-------------------------------------|
|**2026-07-07**|**LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation**|Xinye Yang et.al.|[2607.06323](http://arxiv.org/abs/2607.06323)|null|<think> 好的，用户让我用中文精简总结一篇论文，严格按照【问题】【方法】，总字数控制在300字以内。首先，我需要仔细阅读用户提供的论文摘要，找出核心问题和方法。  论文标题是LAMP，关于通过潜在运动先验指导的实时学习来实现灵巧手操作。摘要里提到现实中的学习容易崩溃，因为高维动作会放大模仿错误，强化学习探索容易导致接触中断。问题应该是高维手部动作导致模仿学习不稳定和强化学习样本效率低、风险高。  接下来看方法部分。他们引入了潜在运动先验模块，将历史动作映射到紧凑的条件潜在先验，解码成高维目标。然后分三阶段：预训练先验，训练视运动政策预测原生臂命令和潜在偏移，最后用在线残差强化学习改进政策。核心创新是共享解码接口，让残差探索在潜在空间局部修正，而不是每个关节独立调整。  用户要求突出核心创新点，避免技术细节。需要确保问题和方法部分简洁，不涉及具体训练步骤。还要注意格式，严格按照【问题】【方法】，在同一行，无换行，不超过300字。  可能用户是研究人员或学生，需要快速了解论文贡献，用于文献综述或项目参考。他们可能希望快速抓住关键点，不需要深入细节。要确保总结准确，特别是潜在先验和三阶段框架，以及最终效果提升的数据。  检查字数，确保符合要求。可能需要调整措辞，比如“高维手部动作导致模仿学习不稳定和强化学习探索低效”来简化问题。方法部分强调潜在先验模块和三阶段框架，以及共享接口的效果。最后结果部分提到成功率提升，但用户要求只到方法，所以可能不需要结论部分？不过用户给的例子有结论，可能需要确认。根据用户提供的示例，他们确实包含了结论，但用户要求的是【问题】【方法】，可能结论是可选的？需要再仔细看用户指示。  用户给的示例输出有【问题】【方法】【结论】，但用户的要求是“严格按照【问题】【方法】，总字数控制在300字以内”。可能用户示例有误，或者可能用户希望包括结论。需要再次确认。根据用户提供的指示，他们要求输出【问题】【方法】，但示例中包含结论。这可能是个矛盾，需要仔细处理。  仔细看用户的问题描述：“请用中文精|
|**2026-07-07**|**Can Reinforcement Learning Efficiently Discover Price Manipulation?**|Ioanna-Yvonni Tsaknaki et.al.|[2607.06121](http://arxiv.org/abs/2607.06121)|null|<think> 好的，我需要帮用户总结这篇论文，按照要求的格式：问题、方法、结论，控制在300字以内，突出核心创新点，避免技术细节。首先，我得仔细阅读用户提供的论文摘要，抓住关键点。  论文的问题是探讨强化学习（RL）能否比传统的基于模型的 方法更有效地发现和利用价格操纵机会。传统方法假设数据生成过程正确，但依赖噪声参数估计，而RL不需要显式模型。接下来，方法部分提到他们在一个单资产市场中测试，价格遵循Almgren-Chriss框架，既有非线性永久冲击又有线性暂时冲击。他们比较了两种方法：模型基于的参数估计和深度确定性策略梯度（DDPG）的RL方法。结论是，在中等波动下，RL无需模型知识就能发现策略，且在参数估计有抽样误差时表现更好，而大波动下所有方法都无效，小波动下模型方法更好。核心创新点应该是RL在复杂控制问题中的有效性，以及在存在参数误差时的优势，同时指出需要安全措施。  现在要精简，确保每个部分简洁。问题部分要说明比较RL和传统方法在价格操纵中的效率。方法部分简要说明实验设置和两种方法。结论强调RL的优势和适用条件，以及安全风险。注意不要技术细节，比如具体的框架名称可能不需要，但用户摘要里提到Almgren-Chriss，可能需要保留，但不确定是否必要。用户要求突出创新点，所以重点在RL的有效性和参数误差下的表现，以及安全警示。  检查字数，确保不超过300字。然后按照格式输出，同一行，无换行，不包含其他解释。可能需要调整措辞，比如“建立存在性并计算基准策略”可以简化为“建立存在性并计算最优策略”。确认所有核心点都涵盖，没有遗漏重要结论。最后检查格式是否符合要求，确保问题、方法、结论正确，用中文，精简。 </think> 问题：比较强化学习与基于模型的参数估计方法在单资产价格操纵识别中的效率差异；方法：构建Almgren-Chriss框架市场，对比参数估计与DDPG强化学习在有限数据下的策略发现能力；结论：中等波动下RL无需模型知识有效识别操纵策略且抗参数误差，大波动下全方法失效，小波动模型方法更优，验证RL在复杂控制中的潜力但警示金融|
|**2026-07-06**|**Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning**|Matthew Foutter et.al.|[2607.04681](http://arxiv.org/abs/2607.04681)|null|<think> 好的，我现在需要处理用户的查询，他要求用中文精简总结一篇论文，严格按照指定的格式，并且控制字数在300字以内。首先，我得仔细阅读用户提供的论文摘要，理解其中的核心内容。  用户给的论文标题是“Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning”，摘要里提到Embodied Chain-of-Thought（SoTA）在机器人决策中的应用，但质疑其是否真正反映内部决策过程。问题在于区分功能推理和忠实推理，指出SoTA对忠实性的策略不足，可能导致中间步骤掩盖因果联系。方法部分他们开发了Pinocchio作为行为批评家，评估观察接地和步骤连贯性，用强化学习进行后训练。结论是后训练提升了忠实性，并在合成数据集上表现更好。  接下来，我需要按照用户指定的格式：问题、方法、结论，每部分用方括号括起来，内容精简，突出创新点，避免技术细节。用户强调要在一行内输出，不要换行，所以需要确保各部分用竖线分隔，并且总字数不超过限制。  首先，问题部分要简明指出当前SoTA的不足，即功能推理与忠实推理的差距，导致中间步骤可能不真实。方法部分要提到Pinocchio作为行为批评家，用于评估和强化学习后训练。结论部分则强调提升的指标和效果，如4%、18%的提升，以及合成数据集的1.6倍响应。  需要注意用户要求避免技术细节，比如具体的评估方法或基准，所以可能需要简化。同时要确保核心创新点突出，比如Pinocchio的使用和后训练策略的有效性。最后检查字数，确保不超过300字，并且格式正确，没有换行符或其他解释。 </think> [问题] SoTA在机器人决策中功能推理与忠实推理存在差距，中间步骤可能掩盖因果联系导致政策泛化受限[方法]提出Pinocchio行为批评家通过观察接地性和步骤连贯性评估忠实性，设计强化学习后训练优化政策[结论]后训练使SoTA模型在驾驶基准中提升4%和18%的忠实性及轨迹误差，合成数据集政策对罕见场景响应增强1.6倍，实现更可靠可解释的具身智能。|
|**2026-07-06**|**PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving**|Pin Tang et.al.|[2607.04637](http://arxiv.org/abs/2607.04637)|null|<think> 好的，我现在需要处理用户的这个请求。首先，用户希望我精简总结一篇关于自动驾驶的论文，严格按照问题、方法、结论的格式，控制在300字以内，并且突出核心创新点，避免技术细节。  首先，我得仔细阅读论文的摘要，理解其中的主要问题和作者提出的方法。论文的标题是PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving。摘要里提到现有的VLAs在预测3D轨迹时存在两个问题：一是2D到3D预测依赖相机参数，导致数据扩展性差；二是直接优化3D空间容易收敛到平凡解，过度依赖车辆状态而非视觉理解。  接下来，作者提出的方法是PixelPilot，核心创新点在于分阶段的规划与提升。规划阶段是2D到2D的任务，避免相机参数的问题，提升阶段在推理时将2D轨迹升维到3D，充分利用视觉信息。另外，他们用了知识注入的策略，通过GRPO优化中间奖励，确保从视觉感知到空间规划的因果链。  现在需要把这些内容浓缩到问题、方法、结论三个部分，每部分简洁明了。问题部分要概括现有方法的两个缺陷，方法部分突出分阶段规划和知识注入策略，结论则强调性能提升和扩展性。  需要注意的是用户要求严格按照格式，所有内容在同一行，无换行符，不包含其他解释。所以必须确保结构正确，语言精炼，同时不超过字数限制。可能还需要检查是否有技术细节需要删减，比如具体的技术名称如GRPO可以保留，但不需要详细解释。  最后，确保总字数在300字以内。现在组合起来：  问题：现有VLA依赖相机参数导致数据扩展性差，且3D优化易收敛平凡解，过度依赖车辆状态。 方法：PixelPilot采用分阶段规划（2D到2D）与升维（仅推理时3D），结合知识注入的GRPO优化因果链。 结论：在开放和闭环测试中表现最佳，验证其扩展性和视觉推理优势。  检查是否符合要求，结构正确，核心点突出，无技术细节，字数应该合适。确认无误后输出。 </think> 问题：现有VLA依赖相机参数导致数据扩展性差，且3D优化易收敛平凡解，过度依赖车辆状态。方法：PixelPilot采用分阶段规划（2D到2|
|**2026-07-05**|**A Perception-Manipulation Robotics System for Food Cutting**|Xinyuan Luo et.al.|[2607.04367](http://arxiv.org/abs/2607.04367)|null|<think> 好的，我现在需要帮用户精简总结一篇论文，按照指定的格式：问题、方法、结论，总字数控制在300字以内。用户特别强调要突出核心创新点，避免技术细节，直接输出总结，并且所有内容在同一行内，不能有换行符或其他解释。  首先，我得仔细阅读用户提供的论文摘要。论文标题是“A Perception-Manipulation Robotics System for Food Cutting”，摘要里提到烹饪机器人中切割任务的关键性，挑战在于食物多样性的处理，需要不同的切割策略和刀具。提出的系统是一个感知-操作框架，包括刀具选择模块和自适应切割阶段。刀具选择模块用初步固定试切的数据来选刀，自适应切割用强化学习平衡速度和能耗。实验显示刀具选择100%成功，并与固定策略、人类操作员比较，性能高且接近人类。  接下来，我需要按照用户给的格式来组织内容。问题部分要简明指出核心挑战，即食物多样性和需要不同刀具策略。方法部分要突出创新点：基于试切的力数据选刀，强化学习自适应切割。结论部分强调高成功率、与人类相当的性能，以及系统的高效性。  需要注意用户要求避免技术细节，比如具体的算法名称可能可以简化，但用户例子中用了强化学习（RL），所以可能需要保留。同时要确保字数在限制内，可能需要精简语言，比如用“自适应强化学习”代替详细描述。  然后检查是否符合格式要求：问题、方法、结论，同一行，无换行，无其他解释。用户给的例子中，每个部分用方括号括起，中间用竖线分隔，所以需要严格按照这个格式。同时总字数要控制在300字以内，但用户提供的例子显然更短，所以可能实际需要更简洁。  最后，确保没有遗漏核心创新点：刀具选择模块的成功率和自适应切割阶段。结论中的实验结果，如100%成功率和与人类相当的性能。可能还需要提到系统的高效性，如平衡速度和能耗。  现在将这些整合成一行，确保每个部分准确，语言精炼，符合用户的所有要求。 </think> 【问题】食物多样性导致需不同切割策略及刀具选择挑战；【方法】基于试切力数据的刀具智能选型+自适应强化学习切割优化；【结论】实现100%未见过食材选刀成功率，切割性能接近人类且兼顾效率|
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
|**2026-07-09**|**DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation**|Yunchao Yao et.al.|[2607.08751](http://arxiv.org/abs/2607.08751)|null|<think> 好的，用户让我用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我需要仔细阅读论文摘要，找出核心内容。  问题部分应该包括现有的不足，比如任务多样性不够，数据覆盖不全，视觉变化不可控，影响跨任务和跨体机的泛化。方法部分要突出DexVerse的创新点，比如100个任务，3种机械臂，6种手型，可扩展，视觉配置，还有各种传感器数据。结论部分则是评估结果，显示方法在任务和视觉上的挑战，以及作为测试床的价值。  要注意避免技术细节，保持简洁。用户强调要严格按照格式，同一行内，不换行，不加解释。所以需要把每个部分压缩成一句话，用【】括起来，中间用逗号分隔。检查字数，确保不超过300字。可能需要调整用词，比如“支持3种机械臂和6种手型”可以简化为“支持3臂6手”。确认核心创新点都涵盖：多任务、多体机、模块化、视觉配置、大量演示数据。最后确保结构正确，没有多余内容。 </think> 【问题】现有 benchmarks 任务与数据多样性不足，缺乏多体机与可控视觉泛化评估【方法】DexVerse 构建包含100项多任务（含抓取、工具使用、双臂协调等）的模块化基准，支持3臂6手扩展，提供可调纹理/光照/视角及多模态传感器数据【结论】评估显示任务与视觉泛化存在显著挑战，验证其作为通用抓取测试床的有效性|
|**2026-07-09**|**FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation**|Shiyuan Yang et.al.|[2607.08575](http://arxiv.org/abs/2607.08575)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，按照问题、方法、结论的格式，控制在300字以内。首先，我得仔细阅读用户提供的资料。  论文标题是FabriVLA，一个轻量级的Vision-Language-Action模型，用于精确的多任务操作。摘要里提到他们结合了InternVL3.5作为视觉语言主干，还有一个流匹配的动作头，用了带门控自注意力的动作令牌和浅层VLM层融合来丰富空间上下文。训练方法是从预训练的VLM开始，单阶段联合优化，随机初始化的动作头。在Meta-World的MT50基准测试中，平均成功率90%，说明在1B规模的VLM基础上构建的紧凑VLA也能达到高性能，不需要大参数的模型。  用户要求突出核心创新点，避免技术细节。所以问题部分要说明传统VLA模型的不足，比如参数量大，难以部署。方法部分要强调他们如何用轻量级结构，结合主干网络和动作头，训练方式。结论则是性能验证和轻量化的优势。  需要注意严格按照格式，同一行内，无换行，无解释。字数要控制，可能需要精简语言。比如问题部分可以写成“传统VLA模型参数量大，难以部署”。方法部分“提出轻量级FabriVLA，融合InternVL3.5与流匹配动作头，单阶段优化预训练VLM”。结论“在MT50上平均成功率90%，验证1B规模VLA可高效实现多任务操作”。  检查是否符合要求：核心创新点是否突出，有没有技术细节，格式是否正确。确认无误后输出。 </think> 问题：传统VLA模型参数量大难以部署方法：提出轻量级FabriVLA融合InternVL3.5与流匹配动作头单阶段优化预训练VLM结论：在MT50上平均成功率90%验证1B规模VLA可高效实现多任务操作|
|**2026-07-08**|**Feedback Manipulation Regularization: Enabling Offline Agent Alignment for Imitation Learning**|Benjamin Poole et.al.|[2607.07859](http://arxiv.org/abs/2607.07859)|null|<think> 好的，我现在需要帮用户总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，而且所有内容要在同一行内，不能换行。用户还特别强调要突出核心创新点，避免技术细节。  先看一下论文的标题和摘要。标题是“Feedback Manipulation Regularization: Enabling Offline Agent Alignment for Imitation Learning”，摘要里提到他们提出了FMR方法，用于利用评估反馈来改善强化学习中的模仿学习策略的对齐问题。现有的方法多使用多阶段管道，而他们探索了单阶段训练中的互补输入。  用户需要的问题部分应该总结现有方法的不足，也就是问题。这里的问题应该是现有方法多阶段处理，而单阶段在完全序列决策环境中缺乏整合互补信号的研究。方法部分就是提出的FMR算法，利用评估反馈作为校正信号，适应Safety Gymnasium环境，减少不匹配，并且适用于有限数据。  需要注意避免技术细节，比如具体如何适应环境或者算法细节，只保留核心创新点。同时要检查字数，确保不超过300字。现在需要把问题、方法、结论用简洁的语言表达出来，并且合并成一行，不换行。  可能的结构：问题部分说明现有方法的问题，方法部分说明FMR的创新，结论部分说明效果和适用性。例如：  问题：现有方法多阶段整合反馈与示范，单阶段 offline 环境中互补信号未充分研究；方法：提出FMR算法利用评估反馈校正策略，适配安全环境验证；结论：显著提升对齐效果，98%减少不匹配，有限数据有效。  检查是否符合要求，有没有遗漏核心点，比如算法无关、有限数据鲁棒性。可能需要调整措辞，确保在字数限制内。最终确保问题、方法、结论各部分清晰，没有技术细节，符合用户格式要求。 </think> 问题：现有方法多阶段整合反馈与示范信号，单阶段 offline 环境中互补信号未充分研究；方法：提出反馈操纵正则化算法FMR利用评估反馈校正策略，适配安全环境验证；结论：显著提升对齐效果98%减少不匹配，有限数据有效。|
|**2026-07-08**|**Shift & Drift: A Zero-Shot Benchmark for Generalizable and Robust Autonomous Driving Motion Planning**|Alessandro Canevaro et.al.|[2607.07844](http://arxiv.org/abs/2607.07844)|null|<think> 好的，我现在需要处理用户的这个请求，帮他精简总结一篇论文。首先，我得仔细阅读用户的要求，确保完全理解。用户希望用中文精简总结论文，严格按照【问题】【方法】，总字数控制在300字以内，并且要突出核心创新点，避免技术细节，直接输出总结，格式是三部分在同一行，没有换行符。  首先，我需要通读论文的摘要，抓住核心内容。论文标题是“Shift & Drift: A Zero-Shot Benchmark for Generalizable and Robust Autonomous Driving Motion Planning”。摘要中提到，现有的基于大规模数据集的闭环运动规划器（如nuPlan）在分布内（ID）表现良好，但缺乏对新型城市拓扑结构和执行扰动后恢复机制的研究。为此，作者提出了Shift & Drift，一个双轨道的基准测试，用来测试运动规划器在语义偏移和状态分布偏移上的鲁棒性。  接下来，我需要按照用户指定的格式来组织内容。问题部分要说明研究的核心挑战，方法部分要概述创新的方法，结论部分总结主要发现。需要注意的是，用户要求突出核心创新点，避免技术细节，所以需要提炼关键信息，比如双轨道基准、零样本评估、强化学习规划的优越性等。  然后，我需要检查字数是否符合要求。用户要求总字数在300字以内，所以要精炼语言，确保每个部分简洁。例如，问题部分可以写成“闭环运动规划器在语义偏移（跨区域场景）和执行扰动（动态噪声）下的泛化与鲁棒性不足”，方法部分则是“提出双轨基准Shift & Drift：语义偏移轨通过转换3D数据集评估跨区域泛化；状态偏移轨注入动态噪声量化鲁棒性”，结论部分“强化学习规划器在偏移下退化更平缓，验证了模仿学习高ID精度但泛化差、漂移明显，强化学习平衡安全与效率的实证权衡”。  最后，要确保格式正确，所有内容在同一行，没有换行符，并且严格按照用户提供的结构。需要多次检查是否有遗漏的核心创新点，比如零样本评估、两种偏移类型的测试，以及对比不同方法的表现。同时，避免使用专业术语过多，保持语言简洁明了。确认无误后，输出最终结果。 </think> 【问题】闭环运动规划器在语义偏移（|
|**2026-07-07**|**LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation**|Xinye Yang et.al.|[2607.06323](http://arxiv.org/abs/2607.06323)|null|<think> 好的，我现在需要处理用户的请求，帮他精简总结一篇论文。首先，我要仔细阅读用户提供的资料，确保理解他的要求。  用户给了一个论文的标题、摘要，还有具体的格式要求：用中文，分问题、方法、结论三部分，每部分用方括号括起来，总字数控制在300字以内。而且要突出核心创新点，避免技术细节，严格按照格式输出，所有内容在同一行，不要换行和其他解释。  首先，我需要从摘要中提取关键信息。论文的问题是关于现实中的灵巧手学习容易崩溃，因为高维动作放大模仿错误，强化学习探索容易导致接触中断。然后方法是引入一个潜在运动先验模块，将近期手部动作历史映射到一个紧凑的条件潜在先验，解码连续潜在命令为可执行的高维目标。接着是三阶段框架：预训练潜在先验，训练视运动策略预测原臂命令和潜在动作偏移，最后用在线残差强化学习改进策略。最后结论是在四个任务上表现优异，成功率从56.25%提升到98.75%甚至100%。  接下来要确保符合用户的要求。用户强调要突出核心创新点，所以需要把潜在运动先验模块和三阶段框架作为重点，避免详细的技术步骤。同时要严格控制在300字以内，所以需要精简语言，合并重复的信息。  然后检查格式是否正确，问题、方法、结论是否清晰，是否在同一行，没有换行符。还要确保没有包含其他解释，直接输出总结内容。  可能需要注意的细节是，用户提到“所有内容在同一行内，不要包含换行符”，所以需要用空格分隔各部分，而不是换行。例如，用【问题】...【方法】...【结论】这样的结构，中间用空格分隔，而不是换行。  最后再通读一遍，确保没有遗漏关键点，字数符合要求，格式正确。比如，问题部分要说明高维动作导致的问题，方法部分强调潜在先验和三阶段框架，结论部分突出成功率和任务数量。确保核心创新点如潜在先验模块、共享解码接口、残差强化学习都被提到，但不过多展开技术细节。 </think> [问题]高维灵巧手动作放大模仿误差且强化学习易因接触中断导致失败，传统方法依赖大量人工监督且探索效率低|
|**2026-07-06**|**Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation**|Jiaqi Peng et.al.|[2607.05377](http://arxiv.org/abs/2607.05377)|null|<think> 好的，我现在需要帮用户精简总结这篇论文，按照要求的格式来。首先，用户给的论文标题是关于Cortex框架的，解决长周期操作的问题。摘要里提到的问题在于现有的VLA模型因为马尔可夫性质难以处理长任务，而分层方法存在高阶规划和低阶执行之间的差距。  接下来，我需要确定问题和方法部分。问题部分要突出长任务处理困难，高阶与低阶不匹配。方法部分要强调Cortex的双向对齐框架，32个技能原语，数据生成中的可执行性原则，事件平衡采样和任务上下文到约束的工程。结论则是性能提升，零样本完成新任务。  用户要求严格控制在300字以内，避免技术细节，突出创新点。需要检查是否遗漏了核心点，比如自动标注数据、仿真数据生成，以及闭环和开环评估的结果。还要注意格式，严格按照问题、方法、结论的顺序，同一行不换行，不包含其他解释。  可能需要注意术语的简化，比如“Markovian nature”翻译为“马尔可夫特性”是否合适，或者是否需要更通俗的说法。但用户要求用中文，所以保持专业术语的准确性。最后确保字数符合要求，可能需要调整句子结构，使其更简洁。 </think> 问题：VLA模型长任务处理困难且高阶规划与低阶执行不匹配；方法：Cortex框架双向对齐技能原语、数据生成注入可执行性原则、事件平衡采样及任务约束工程；结论：显著提升性能且支持零样本完成多阶段长任务。|
|**2026-07-06**|**KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation**|Xinyu Shao et.al.|[2607.04652](http://arxiv.org/abs/2607.04652)|null|<think> 好的，我现在需要帮用户总结这篇论文。首先，用户的要求很明确，用中文精简总结，严格按照问题、方法、结论的格式，控制在300字以内，突出核心创新点，避免技术细节，并且所有内容在同一行，不要换行符。  首先，我得仔细阅读论文摘要。论文标题是KAM-WM，主要解决机器人在抓取任务中需要视觉先验的问题。问题部分应该包括当前方法的不足，比如静态的分割掩码只能定位区域，无法指导如何开始交互。方法部分要提到他们提出的框架，从冻结的视频世界模型中提取Kinematic Affordance Map（KAM），使用Flow Matching和Perceiver压缩，结合扩散策略。结论部分则是实验结果和意义，比如在LIBERO和RoboTwin上的表现，以及方向信息的贡献。  接下来要确保核心创新点突出。用户强调避免技术细节，所以不需要提到Flow Matching的具体实现，而是说“基于冻结视频世界模型”和“单步隐式速度”。结论中的比较结果和意义也要简明，比如提到部分增益来自方向信息。  然后检查格式是否符合要求。问题、方法、结论三个部分，用竖线分隔，全部在同一行，没有换行。字数要控制在300字以内，现在大概的总结可能需要调整，确保简洁。  可能需要注意术语的准确翻译，比如“Kinematic Affordance Map”翻译为“运动功能图”，“Perceiver”可能不需要翻译，保留英文。另外，实验数据如成功率要准确无误，单位也要正确。  最后，检查是否有冗余信息，比如“without rollout or world-model fine-tuning”可以简化为“无需回滚或世界模型微调”，但用户要求避免技术细节，可能可以省略，但关键点如“冻结模型”需要保留。确保每个部分的信息都准确且简洁，符合用户的要求。 </think> 问题：现有静态视觉先验仅定位抓取区域无法指导初始动作；机器人抓取需融合交互位置与初始动作方向。方法：提出KAM-WM框架，基于冻结视频世界模型单步隐式速度生成运动功能图（KAM）指导交互，结合Perceiver压缩与扩散策略控制。结论：在LIBERO和RoboTwin2.0上平均成功率90.6%和65.7%-22.4%，验证方向信息对动作|
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

