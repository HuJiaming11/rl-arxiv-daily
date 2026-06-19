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

## Updated on 2026.06.19
> Usage instructions: [here](./docs/README.md#usage)

## Reinforcement Learning

| Publish Date | Title | Authors | PDF | Code | 摘要 |
|:---------|:-----------------------|:---------|:------|:------|:-------------------------------------|
|**2026-06-18**|**Generating Robot Hands from Human Demonstrations**|Sha Yi et.al.|[2606.20549](http://arxiv.org/abs/2606.20549)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结这篇论文。首先，用户的要求很明确，要严格按照【问题】【方法】，总字数控制在300字以内，突出核心创新点，避免技术细节，并且直接输出总结内容，所有内容在同一行内，不要换行和其他解释。  首先，我得仔细阅读论文的摘要，理解核心内容。论文的问题是关于机器人手的学习，传统方法需要同时设计结构和控制，导致组合问题复杂。作者提出了一种数据驱动的框架，从人类示范中生成机器人手。关键点在于使用逆运动学匹配指尖位置，而不是同时学习控制器和设计。方法部分提到了使用超过400万帧的人类手势数据，优化树状结构的手，训练强化学习演员来加速设计搜索，并直接打印成一体结构。结论是生成的6-DoF手跟踪精度高，3-DoF手机械复杂度低，验证了大数据在生成物理结构中的应用。  接下来需要按照用户给的格式来组织内容。问题部分要简明指出传统方法的困难，即设计控制联合优化困难。方法部分要突出核心创新：数据驱动生成，逆运动学匹配，强化学习加速搜索，直接打印。结论部分强调生成的手性能优于商用，验证大数据生成物理结构的有效性。  要注意避免技术细节，比如具体的DoF数量、训练数据的具体处理方式等，保持简洁。同时确保总字数在300字以内，可能需要多次精简。检查是否有冗余信息，比如“print-in-place joints”可以简化为“直接打印”，而“real-world experiments”可以省略，因为结论已经提到验证了效果。  最后，确保严格按照格式输出，所有内容在同一行，没有换行符，不包含其他解释。可能需要调整措辞，确保每个部分准确且连贯。例如，问题部分要明确传统方法的难点，方法部分突出创新点，结论部分强调结果和意义。检查字数，确保符合要求。 </think> 【问题】机器人手设计需同时优化结构和控制，存在复杂组合问题；【方法】基于400万帧人类指尖数据，通过逆运动学生成树状手结构，强化学习演员加速设计搜索，直接打印一体化关节；【结论】6-DoF手实现高精度指尖跟踪，3-DoF手机械复杂度低，验证大数据驱动生成物理结构有效性。|
|**2026-06-18**|**A Neuromorphic Reinforcement Learning Framework for Efficient Pathfinding in Robotic Mobile Fulfillment Systems**|Junzhe Xu et.al.|[2606.20031](http://arxiv.org/abs/2606.20031)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我得仔细阅读论文摘要，抓住核心内容。  问题部分：动态环境变化、狭窄工作空间和实时限制导致传统方法计算复杂高，决策延迟大。虽然强化学习（RL）有潜力，但部署到低功耗硬件仍有挑战。  方法部分：他们提出了SDQN-RMFS框架，通过允许碰撞的策略训练ANN，然后用知识蒸馏转成SNN，只在事件触发时计算，实现低功耗路径规划。  结论部分：实验显示比GPU节能11281倍，延迟几乎翻倍，决策质量相当，证明神经形态推理可行。  要注意突出创新点，避免技术细节。用户要求严格格式，同一行不换行，所以需要把三个部分用【】括起来，中间用|分隔。检查字数，确保不超过300字。可能用户是机器人或自动化领域的研究者，需要快速了解论文贡献，所以重点在问题、方法和结论的创新，以及实验结果。需要确认术语准确，比如“神经形态芯片”是否正确，摘要里用的是“neuromorphic chip”，所以翻译成“神经形态芯片”没问题。最后检查格式是否符合要求，没有换行，没有多余解释。 </think> 【问题】动态环境变化、狭窄工作空间和实时约束导致传统路径规划方法计算复杂且延迟高，强化学习部署在低功耗硬件存在能效挑战|【方法】提出SDQN-RMFS框架，通过允许碰撞训练高信息量轨迹的ANN，经知识蒸馏转换为SNN并触发式计算，实现神经形态芯片低功耗推理|【结论】较GPU节能11281倍，延迟降低近两倍且决策质量相当，验证神经形态推理在大型RMFS中的可持续性|
|**2026-06-16**|**WireCraft: A Simulation Benchmark for Industrial DLO Manipulation**|Chongyu Zhu et.al.|[2606.18097](http://arxiv.org/abs/2606.18097)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结一篇论文。首先，我得仔细阅读用户的要求。用户希望用中文，严格按照【问题】【方法】，总字数控制在300字以内，并且要突出核心创新点，避免技术细节。输出格式必须严格按照指定，同一行内，不要换行，不要其他解释。  首先，我需要解析论文的摘要。论文标题是“WireCraft: A Simulation Benchmark for Industrial DLO Manipulation”。摘要里提到的问题在于现有的工业变形物体（DLO）操纵基准存在不足，比如依赖特定硬件、缺乏模块化任务资产、未考虑实际工业中的夹具等。方法部分介绍了WireCraft，包含三个任务家族，两种物理模型，以及不同政策的评估。结论指出虽然特权状态RL表现好，但视觉类方法在连接器插入的对接阶段存在瓶颈。  接下来，我需要按照用户指定的格式来组织内容。问题部分要简明扼要，突出现有基准的不足。方法部分要说明WireCraft的创新点，比如模块化任务、多物理模型、多数据源评估。结论部分要总结主要发现，特别是视觉方法的挑战。  要注意避免技术细节，比如具体的物理模型名称（articulated和deformable）可能不需要详细说明，可以简化为“多物理模型”。同时，用户强调核心创新点，所以需要突出WireCraft的模块化、多任务、多模型和数据共享这些方面。  然后检查字数，确保不超过300字。可能需要多次精简，比如将“支持两种互补的DLO物理模型”改为“多物理模型”，或者“从仿真和物理UR5获取轨迹”简化为“多数据源评估”。同时，保持语句连贯，符合中文表达习惯。  最后，确保严格按照格式输出，所有内容在同一行，没有换行符，没有其他解释。可能需要调整措辞，确保每个部分的信息准确且符合用户要求。例如，问题部分要明确现有基准的三个问题，方法部分强调WireCraft的三个任务家族和评估方法，结论部分指出视觉方法的瓶颈和基准的开源计划。  现在，整合所有信息，确保每个部分的信息准确，语言简洁，符合格式要求。检查是否有遗漏的核心创新点，比如共享评估协议和开源计划，这些都需要包含在结论中。最终形成符合用户要求的总结。 </think> 【问题】工业变形物体（DLOs|
|**2026-06-15**|**VENOM: Versatile Embodied Network for Omni-bodied Motion tracking**|Siddharth Padmanabhan et.al.|[2606.16696](http://arxiv.org/abs/2606.16696)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照【问题】【方法】，总字数控制在300字以内。首先，我得仔细阅读用户提供的论文摘要，抓住核心内容。  论文的问题是关于多机器人体的全身运动跟踪，特别是使用演示数据实现专家级别的表达性跟踪，而现有的方法通常将控制问题分解为上下身控制，存在不足。用户要求突出核心创新点，避免技术细节，所以我要确保总结不涉及太多技术术语，只保留关键点。  接下来是方法部分。论文提出VENOM模型，基于GPT的全身运动跟踪器，不需要分解上下身控制。他们还创建了一个多机器人体数据集VENOM Dataset，包含状态、动作和奖励，训练了VENOM和基线模型。实验结果显示VENOM性能优于MLP监督学习，且在无奖励反馈的情况下接近专家水平。  现在需要将这些信息浓缩成问题和方法，同时符合格式要求。问题要明确当前研究的挑战，方法要突出创新点如GPT模型和数据集。要注意字数限制，确保不超过300字，并且所有内容在同一行，不换行，不加其他解释。  检查是否有遗漏的核心创新点：GPT-based、跨身体控制、无需分解、多机器人数据集、对比基线结果。这些都要包含进去。避免技术细节如具体的算法结构或训练过程，保持简洁。  最后，确认格式是否正确，是否严格按照用户提供的模板，确保没有换行符或多余的解释。现在可以组合成最终的总结。 </think> 【问题】多机器人体全身运动跟踪需专家级表达且传统方法依赖上下身分解控制存在局限；【方法】提出VENOM基于GPT的跨身体控制模型训练于多机器人数据集VENOM Dataset无需上下身分解，结合状态动作奖励数据；【结论】VENOM在无奖励反馈下实现接近专家能力的稳定跟踪，优于MLP监督学习且适应不同机器人体。|
|**2026-06-15**|**Reinforcement Learning with Inner-loop Dynamics Estimator for Aerial Manipulation under Uncertainty**|Shivansh Pratap Singh et.al.|[2606.16621](http://arxiv.org/abs/2606.16621)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照【问题】【方法】，总字数控制在300字以内。首先，我得仔细阅读用户提供的论文摘要，理解核心内容。  论文的问题是关于无人机机械臂在快速运动、负载变化和动态不确定下的直接 whole-body 操纵难题。现有的方法可能依赖准确的耦合动态模型，这在不确定环境中效果不佳。用户要求突出创新点，避免技术细节，所以我要抓住关键点：问题在于直接控制中的模型不准确，方法则是分层框架结合强化学习和内环动态估计器。  接下来，我需要按照格式来组织内容。问题部分要简明，说明在动态不确定条件下的直接控制困难。方法部分要强调分层框架，外环用RL映射目标到指令，内环用估计器补偿不确定性。结论部分要指出结合学习和估计器提高了精度和鲁棒性。  要注意字数限制，总字数300以内，所以每部分要简洁。可能需要调整用词，比如“动态不确定”代替更长的描述。同时检查是否符合用户格式要求，所有内容在同一行，无换行，无其他解释。  最后，确保核心创新点突出：分层控制、RL外环和估计器内环的结合，以及实验验证的结果。避免提到PID和INDI+PID等细节，只保留关键比较结果，如跟踪误差减少和任务成功率提升。检查格式是否正确，有没有遗漏的部分，确保完全符合用户的要求。 </think> 【问题】无人机机械臂在快速运动、负载变化及动态不确定条件下实现直接 whole-body 操纵存在难题，传统方法依赖精确动态模型且控制精度不足【方法】提出分层控制框架，外环通过强化学习将末端执行器目标映射为协调指令，内环基于动态估计器补偿执行中的惯性偏移和不确定性，无需系统模型知识【结论】实验表明结合学习协调与估计器补偿可降低跟踪误差提升任务成功率，验证分层结构在动态环境下的鲁棒性和精度优势|
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
|**2026-06-18**|**CoLI: A Reproducible Platform for Continuum Robot Learning via Monolithic 3D Printing and Isomorphic Teleoperation**|Ziyuan Tang et.al.|[2606.20389](http://arxiv.org/abs/2606.20389)|null|<think> 好的，用户让我用中文精简总结这篇论文，严格按照【问题】【方法】，总字数控制在300字以内。首先，我需要仔细阅读论文摘要，抓住核心问题和方法。  论文标题提到CoLI平台，使用单块3D打印和同构远程操作。摘要里说连续机器人因为制造复杂、建模困难和使用不直观，导致应用受限。问题应该围绕这三个方面：制造复杂性、建模挑战和控制界面。  方法部分，他们提出了一个开源设计，简化制造流程，通过多材料3D打印实现单块结构，减少组装步骤。控制方面用同构远程接口，直接映射执行器，避免显式运动学建模，消除奇点。还有基于模仿学习的自主控制，硬件评估和任务测试。  结论需要突出成果：可重复、学习准备好，加速算法开发和基准测试。用户要求避免技术细节，所以不用提具体实验结果，只说效果。  现在要检查格式是否正确，问题、方法、结论是否清晰，字数是否符合。确保在同一行，无换行，没有其他解释。核心创新点是单块3D打印和同构接口，还有模仿学习支持。可能用户是机器人领域的研究者或开发者，需要快速了解论文贡献，所以总结要突出实用性和创新点，帮助他们决定是否应用或进一步研究。 </think> 【问题】连续机器人因复杂制造、运动学建模困难和缺乏直观控制导致应用受限【方法】提出基于单块多材料3D打印的简化制造流程和同构远程操作接口实现直接执行器映射，结合模仿学习支持自主控制【结论】构建可重复、学习准备好的连续机器人平台加速算法开发和社区基准测试|
|**2026-06-18**|**Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation**|Jianing Guo et.al.|[2606.20135](http://arxiv.org/abs/2606.20135)|null|<think> 好的，我现在需要帮用户总结这篇论文，按照指定的格式来。首先，用户的要求很明确，要精简总结，控制在300字以内，严格按照【问题】【方法】，总字数不超过。而且用户强调要突出核心创新点，避免技术细节，直接输出，不能有换行符或其他解释。  首先，我得仔细阅读论文的摘要，抓住核心问题和方法。论文标题是“Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation”，摘要里提到现有方法依赖离散动作片段，导致对异构频率演示鲁棒性差，动作不一致影响稳定性。问题就是现有的flow matching方法处理不同频率的演示数据时不够灵活，生成的动作可能不一致。  接下来是方法部分。论文提出FAFM，主要创新点有两个：一是用DCT将离散动作转换到频域，处理异构频率；二是通过正则化一阶导数来平滑动作，对应Sobolev约束，抑制高频误差。方法部分需要简洁，不涉及技术细节，比如DCT和Sobolev约束这些术语可以保留，但不用详细解释。  然后结论部分要说明FAFM的效果，比如在多个基准测试和真实机器人上表现更好，成功率高，多模态，收敛快，鲁棒性强。结论要简短，突出结果。  现在需要把问题、方法、结论整合成三部分，每部分用方括号括起来，所有内容在同一行，没有换行符。要注意字数，可能需要调整用词，比如“离散化动作片段”可以简化为“依赖离散动作片段”，“离散余弦变换（DCT）”可以保留，但可能用户希望更简洁，所以可能直接写“DCT转换频域”。  检查是否符合格式要求，是否有换行符，是否超过300字。可能需要多次调整，比如问题部分：“现有flow matching方法依赖离散化动作片段，导致异构频率演示鲁棒性差，动作不一致影响稳定性。”方法：“FAFM通过DCT转换频域处理异构频率，正则化一阶导数实现平滑动作，抑制高频误差。”结论：“实验表明FAFM提升成功率、多模态性、平滑度及鲁棒性，在真实机器人上验证有效。”  最后确保总字数在300以内，所有内容紧凑，没有多余的解释。可能用户希望核心创新点突出，所以方法|
|**2026-06-18**|**Co-policy: Responsive Human-Robot Co-Creation for Musical Performances**|Xuetao Li et.al.|[2606.19914](http://arxiv.org/abs/2606.19914)|null|<think> 好的，我现在需要帮用户精简总结这篇论文，严格按照【问题】【方法】，总字数控制在300字以内。首先，我要仔细阅读用户提供的论文摘要，理解核心内容。  论文标题是Co-policy: Responsive Human-Robot Co-Creation for Musical Performances。摘要提到，艺术是人类创造力的表达，而具身人工智能通过物理动作让生成模型参与其中，而不是仅仅数字内容。问题在于将语义音乐理解与实时物理执行联系起来。现有的方法可能不够高效，需要更好的框架。  用户要求突出核心创新点，避免技术细节。所以我要找出问题和方法的关键部分。问题部分应该说明当前在音乐人机协作中的挑战，比如语义理解与实时执行之间的鸿沟。方法部分要提到Co-policy框架，分三部分：语义意图锚定、约束音乐变体、视觉运动执行。特别是GMP策略，生成多模态动作，同时考虑音乐和物理约束。  结论部分需要总结实验结果，比如意图对齐、执行准确性和响应频率的提升。要注意不要用技术术语，保持简洁。同时要确保所有内容在同一行，不换行，格式正确。  现在检查字数，确保不超过300字。可能需要调整用词，比如“具身人工智能”可以简化为“具身AI”或者“机器人”，但用户给的例子用了“具身人工智能”，所以保持一致。确保每个部分不超过限定的内容，比如问题部分不超过两句话，方法部分分点但用逗号分隔，结论同样。  最后，验证是否符合用户格式要求，没有换行，没有多余的解释，核心创新点突出。比如Co-policy的三个模块和GMP策略是关键，必须包含。实验结果部分要简明提到对比基线，显示优势。 </think> 【问题】具身人工智能在音乐人机协作中面临语义理解与实时物理执行脱节，传统系统难以生成符合物理约束的互补音乐响应【方法】提出Co-policy框架，通过语义锚定模块（F-Qwen规划器）将多模态输入转化为结构化计划，结合高斯混合视觉运动策略（GMP）单次正向映射生成多模态动作，实现音乐与物理双约束下的实时响应【结论】实验表明其意图对齐度、执行精度和响应频率均优于扩散策略与基线模型，验证了物理执行对具身人机协作的关键|
|**2026-06-17**|**Invertible Neural Network Adapter for One-Step Flow Matching in Robot Manipulation**|Yu Zhang et.al.|[2606.19194](http://arxiv.org/abs/2606.19194)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内，突出核心创新点，避免技术细节。首先，我得仔细阅读论文摘要，抓住关键点。  论文标题是关于可逆神经网络适配器在机械臂操作中的一步流匹配。摘要里提到他们设计了一个可逆的适配器，通过一步去噪过程生成高维动作，结合多种模态输入（视觉、语言、本体感觉）。方法部分是基于流匹配框架，约束动作生成轨迹在可逆潜在空间里，这样单次推理就能高效合成灵巧动作。相比传统迭代方法，复杂度降低但保持高准确性和稳定性。实验部分在仿真和真实平台都做了测试，仿真表现优异，真实场景中推理延迟从110ms降到61ms，性能仍然不错。  接下来要提炼问题、方法和结论。问题应该是机械臂操作中需要多模态输入生成精确动作，传统方法可能迭代步骤多，效率低。方法的核心创新是可逆适配器，一步去噪，流匹配约束潜在空间。结论是实验证明在仿真和真实环境中效果更好，延迟降低，性能保持。  需要注意用户要求所有内容在同一行，无换行，不要其他解释。要确保核心创新点突出，比如可逆性、单步流程、效率提升。避免技术术语如“flow-matching formulation”可能需要简化为“流匹配框架”。同时检查字数，确保不超过300字。  现在组织语言：问题部分说明需求，方法强调创新点和优势，结论突出实验结果。例如：  问题：机械臂需多模态输入生成高精度动作，传统方法效率低、步骤多。 方法：提出可逆神经网络适配器，基于流匹配约束潜在空间，单步去噪生成动作，降低复杂度。 结论：仿真和真实实验均表现优异，推理效率提升45%（延迟从110到61ms），性能稳定。  检查是否符合要求，核心点是否突出，有没有多余细节。确认格式正确，没有换行，总字数在限制内。 </think> 问题：机械臂需多模态输入生成高精度动作，传统方法效率低、步骤多；方法：提出可逆神经网络适配器，基于流匹配约束潜在空间实现单步去噪动作生成，降低复杂度；结论：仿真与真实实验均优于传统|
|**2026-06-16**|**WireCraft: A Simulation Benchmark for Industrial DLO Manipulation**|Chongyu Zhu et.al.|[2606.18097](http://arxiv.org/abs/2606.18097)|null|<think> 好的，我现在需要处理用户的请求，帮他精简总结一篇论文。首先，用户的要求很明确，要按照【问题】【方法】，总字数控制在300字以内，并且严格按照格式输出，不能有换行符或其他解释。我得仔细分析用户提供的论文摘要，找出核心问题和方法，同时忽略技术细节。  首先看论文标题是“WireCraft: A Simulation Benchmark for Industrial DLO Manipulation”。摘要里提到的问题是关于变形线性对象（DLOs）在工业装配中的挑战，现有的基准存在硬件特定、缺乏模块化任务资产、未考虑真实工装夹具等问题，导致政策开发和比较困难。核心问题应该是工业DLO操作缺乏通用、模块化的基准，且缺乏跨模拟与现实的数据和评估协议。  接下来是方法部分，论文提出了WireCraft基准，包含三个任务家族：连接器插入、夹子路由和通道就座。支持两种物理模型（articulated和deformable），数据来自模拟和UR5机器人。评估了RL、IL和VLA策略，使用共享指标，并发现特权状态RL在任务中表现良好，但视觉方法在连接器插入时遇到瓶颈。  需要确保总结中突出创新点，比如模块化任务资产、跨模拟与现实数据、共享评估协议，以及不同模型和策略的对比。避免技术细节如具体成功率数字，但保留关键结果如视觉方法的瓶颈。  然后检查格式是否符合要求，确保问题、方法、结论各部分用【】括起，内容连贯，字数不超过限制。可能需要注意术语的准确性和简洁性，比如“DLO”是否需要全称，但用户示例中用了缩写，所以保持原样。  最后，确保没有换行符，所有内容在同一行，用空格分隔。可能需要多次调整措辞，确保信息完整且符合格式。例如，问题部分要涵盖现有基准的不足，方法部分强调WireCraft的创新和评估，结论指出视觉方法的挑战和基准的贡献。 </think> 【问题】工业变形线性对象（DLOs）操作缺乏通用模块化基准，现有研究受限于特定硬件、缺乏真实工装夹具支持及跨模态数据与评估协议；视觉方法在接触丰富场景中表现不足【方法】提出WireCraft基准，涵盖连接器插入/夹子路由/通道就座三大任务，集成可配置物理模型（articulated/de|
|**2026-06-16**|**LAGO Policy: Latency-Aware Asynchronous Diffusion Policies with Goal-Directed Collision-Free Planning for Smooth Manipulation**|Guowei Shi et.al.|[2606.17982](http://arxiv.org/abs/2606.17982)|null|<think> 好的，我现在需要处理用户的查询，帮他精简总结一篇论文。首先，我要仔细阅读用户的要求，确保完全理解。用户希望用中文，严格按照【问题】【方法】，总字数控制在300字以内，并且突出核心创新点，避免技术细节。同时，必须严格按照指定的格式输出，所有内容在同一行，不要换行符或其他解释。  首先，我需要分析提供的论文摘要。论文标题是LAGO Policy，主要解决异步扩散政策在执行时出现的动作不连续和缺乏障碍物感知的问题。问题部分应该包括这两个主要痛点：动作不连续导致不流畅和碰撞风险。方法部分要突出他们的三个核心创新：延迟感知的引导条件、基于示范的任务相关交互目标预测，以及时空轨迹优化。结论需要总结实验结果，即高效且安全的执行。  接下来，我要确保问题和方法部分准确且简洁，不超过字数限制。需要检查是否有冗余技术术语，用更通俗的语言表达，比如“异步推理”可以简化为“异步推理”。同时，要确保核心创新点如延迟感知、目标预测和优化步骤都被明确提到。  然后，验证是否符合格式要求：问题、方法、结论三个部分，用方括号括起，内容连贯，同一行，无换行。还要检查字数，确保不超过300字。可能需要多次调整措辞，比如将“integrated trajectory optimization”简化为“集成轨迹优化”等。  最后，确认是否遗漏了关键点，比如实验结果中的高任务成功率，以及项目网站链接是否需要包含。根据用户要求，链接可能不需要，但需要确认摘要中的内容是否足够。用户示例中结论部分提到了“高效且安全的执行”，所以可能不需要包含链接。  现在，整合所有信息，确保每个部分都准确且符合要求，最终输出一个简洁、符合格式的总结。 </think> 【问题】异步扩散政策存在动作不连续导致不流畅和碰撞风险，缺乏障碍感知与目标导向规划；【方法】LAGO Policy通过延迟感知引导未来动作、基于示范预测任务交互目标、集成时空轨迹优化提升流畅性与安全性；【结论】实验验证其实现高效且安全的复杂场景抓取，任务成功率显著优于基线。|
|**2026-06-16**|**When Robots Sleep: Offline Skill Consolidation for Shared-Policy Robot Learning**|Nethmi Jayasinghe et.al.|[2606.17493](http://arxiv.org/abs/2606.17493)|null|<think> 好的，我需要帮用户用中文精简总结这篇论文，严格按照问题、方法、结论的格式，控制在300字以内。首先，我得仔细阅读论文摘要，抓住核心内容。  问题部分，用户提到机器人长期部署时需要学习新技能而不破坏共享策略结构，导致相关技能可靠性下降。这里的关键点是不能用任务特定的头部或适配器，且无法获取之前的轨迹和损失，这可能导致技能耦合崩溃。  方法部分，论文提出睡眠机器人的框架，分为醒态和睡眠阶段。醒态学习新技能，睡眠阶段通过冻结的技能记忆进行离线巩固。这里要突出使用无序状态缓冲和观察缓冲，以及通过纳什议价结合梯度，还有自适应锚定和局部兴奋性来稳定巩固。技术细节要简化，比如不提具体的Meta-World MT5和SurgicAI，只说提升效果。  结论部分，需要说明方法在多个基准上的优势，比如平均成功率提升64%，相关技能可靠性翻倍，同时保持向后迁移能力。要避免具体数据，但用户给的摘要里有具体数字，可能需要保留关键数据，比如x2.0，但用户要求避免技术细节，可能得模糊处理，比如“显著提升”或“大幅提高”。  然后检查是否符合格式要求：问题、方法、结论，同一行，无换行，不包含其他解释。核心创新点是醒睡框架和冻结记忆结合纳什议价，要突出这点。可能用户给的例子中结论部分有具体数据，但用户要求避免技术细节，所以可能需要调整。但用户示例中的结论用了具体数据，可能允许保留关键结果，比如提升64%和x2.0，但需要确认是否符合要求。根据用户指示，要突出核心创新点，避免技术细节，所以可能数据可以保留，但需要精简。  最后确保总字数在300以内，中文精简。现在组合起来：  问题：长期部署机器人需新增技能同时保持共享策略结构，导致技能耦合可靠性下降； 方法：提出醒睡框架，醒态学习新技能，睡眠态通过冻结技能记忆离线巩固，利用纳什议价结合梯度，自适应锚定和局部兴奋性稳定巩固； 结论：在多个基准上显著提升平均成功率（+64%）和技能可靠性（x2.0），保持向后迁移能力且可靠性竞争。  检查是否符合要求：|
|**2026-06-15**|**Steering Generative Reinforcement Learning into Stable Robotic Controller**|Yixuan Wang et.al.|[2606.16572](http://arxiv.org/abs/2606.16572)|null|<think> 好的，我现在需要帮用户总结这篇论文。首先，用户的要求很明确：用中文精简总结，严格按照【问题】【方法】，总字数控制在300字以内，还要突出核心创新点，避免技术细节，直接输出总结，并且所有内容在同一行内，不要换行。  首先，我得仔细阅读论文的摘要。问题部分主要是说现有的扩散和流生成策略在强化学习中的应用虽然能通过迭代动作生成丰富的随机探索，但随机性不适合高维机器人系统，小动作变化会导致不一致的运动和降低鲁棒性。方法部分，他们提出了SteerGenPO，用隐式空间强化学习框架，将训练好的生成策略引导成鲁棒确定性的控制器。关键点是将随机的隐式采样替换为学习的隐式演员，预测状态相关的隐式输入，分离探索和控制：生成策略在训练时用随机采样探索，部署时用确定性的隐式引导控制。结论部分是在六个Isaac Lab基准和Unitree G1任务上验证，结果显示优于经典RL和生成RL基线，确定性隐式引导带来更稳定的行为和可靠的指令响应。  接下来要确保总结符合格式，问题、方法、结论各部分要简洁。用户强调要突出核心创新点，所以需要抓住替换随机采样为隐式演员，分离探索和控制这两个关键点。避免技术细节，比如具体的隐式空间框架名称可能可以简化，但用户给的例子中用了SteerGenPO，所以可能需要保留。同时要检查字数，确保不超过300字。  然后，按照用户要求，所有内容在同一行，不换行，没有其他解释。可能需要多次调整措辞，确保信息准确且符合格式。比如问题部分要简明，方法部分突出替换和分离，结论部分强调结果和优势。最后检查是否符合所有要求，比如没有换行符，没有多余的解释，核心创新点是否突出。 </think> 【问题】高维机器人系统中生成强化学习策略的随机性导致动作累积不稳定，降低控制鲁棒性；【方法】提出SteerGenPO通过隐式演员预测状态依赖隐式输入替代随机采样，分离训练时随机探索与部署时确定性隐式引导控制；【结论】在六项基准任务和Unitree G1上实现更稳定运动与可靠指令响应，优于经典RL和生成RL基线。|
|**2026-06-15**|**APEX: Adaptive Policy Execution for Precise Manipulation**|Mengfei Zhao et.al.|[2606.16504](http://arxiv.org/abs/2606.16504)|null|<think> 好的，我现在需要帮用户精简总结这篇论文，按照指定的格式。首先，我得仔细阅读用户提供的论文摘要，理解问题和方法的核心。  论文标题是APEX: Adaptive Policy Execution for Precise Manipulation。问题部分提到，现有的模仿学习方法生成高层动作参考，但执行时存在差距，因为政策不了解底层控制动力学，导致动作偏差，影响精度。之前的方法修改政策或控制器，但需要侵入式调整，而用户的问题是在两者都是黑盒的情况下如何解决。  方法部分，APEX是在政策和控制器之间插入一个框架，动态生成可行参考，并在测试时根据状态反馈调整，有收敛保证。结论是实验显示跟踪误差减少41.2%，成功率提升4.8-25.8%。  用户要求突出创新点，避免技术细节，严格格式，同一行，无换行。需要检查是否符合字数限制，300字以内。现在要组织语言，确保问题、方法、结论准确，且简洁。可能需要注意术语的一致性，比如“执行差距”、“黑盒”等。最后确保没有多余的解释，严格按照格式输出。 </think> 问题：高层动作参考与低层控制动力学不匹配导致执行差距，传统方法需修改黑盒政策或控制器；方法：插入APEX框架动态重构可行参考并测试时自适应调整，保证收敛性；结论：跟踪误差降低41.2%，成功率提升4.8-25.8%。|
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

