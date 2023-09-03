# &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;黎明杀机挂机工具【DBD_AFK_TOOL】   

## ※ 注意：挂机行为存在被BAN风险，任何后果与本工具无关。  
## ~☞ 有任何问题请在[Github Issues](https://github.com/maskrs/DBD_AFK_TOOL/issues)中留言，或者在[讨论区](https://github.com/maskrs/DBD_AFK_TOOL/discussions)交流。~  
|工具功能|
|  :----        |
|1.工具实现对局全自动循环|
|2.工具支持全分辨率【16：9】|
|3.实现游戏错误 【断线、断网、错误代码】 重连（返回匹配大厅），并重新开始匹配|
|4.人类上钩三挣扎|
|~5.屠夫无视手电、鞭炮、闪光弹（个别屠夫除外）【裂隙模式】~ 请自行携带光眼|
|~6.血点防溢出插件【超过190万自动消耗血点，小于150万停止，防止溢出和过度消耗】~（已废弃）|

## 基本设置  
★&ensp;如果你是第一次使用本工具，需要先运行 `初始化.exe` 。

★&ensp;运行 *DBD_AFK_TOOL.exe* 文件启动工具。启动时 **关闭代理**。
 
★&ensp;使用本工具请 *游戏内使用中文语言* ！
 
★&ensp;使用本工具请 *关闭滤镜* ！  

★&ensp;以下两个选项务必为 ***100%*** ！  

&emsp;<img src="https://github.com/maskrs/DBD_AFK_TOOL/blob/main/image-foder/%E7%94%A8%E6%88%B7%E8%AE%BE%E7%BD%AE.png" width="570px">

★&ensp;游戏设置——输入绑定——视角 中的 *“向右转”* 和 *“向左转”* 设置为 *“E”* 和 *“Q”* ！ 

&emsp;<img src="https://github.com/maskrs/DBD_AFK_TOOL/blob/main/image-foder/%E7%94%A8%E6%88%B7%E8%AE%BE%E7%BD%AE2.png" width="500px">

★&ensp;使用本工具请 ***全屏【16：9】*** 游戏，在匹配大厅开启工具！

&emsp;<img src="https://github.com/maskrs/DBD_AFK_TOOL/blob/main/image-foder/%E5%A4%A7%E5%8E%85%E5%90%AF%E5%8A%A8.png" width="600px">

## 角色选择   
  
<details>
<summary>检索配置及高级选项的说明</summary>  
<br />
◆&ensp;检索配置

	检索配置文件为“searchfile.txt”，其内已列出标准配置示例，将你没有的屠夫名称从中删去【注意如果有被禁用的屠夫也一并删去】，保存后即完成配置。
	
	※注意：此文件中的屠夫顺序非常重要，请勿调换。

◆&ensp;高级自定义参数【暂无可视化】

	1、“SDparameter.json”文件为高级参数，这个文件非常重要，如果你不知道如何调整，请勿更改。

		如何重置此文件：删除此文件，并重启软件，可使其重新生成。

	2、具体说明：

		-->>值【字符串】 为颜色，-->>值【数字】 为相似度（除特殊说明）。
		---------------------------------------------------------------------

		键“blood”两个为血点检测	区域范围：1105, 0, 1715, 144

		键“ceasma”两个为荧光裂片检测	区域范围：1105, 0, 1715, 144

		键“setting_button”两个为设置按钮检测	区域范围：292, 978, 341, 1032

		键“set_race”两个为对局结束后的设置按钮检测	区域范围：91, 985, 133, 1026

		键“ready”两个为准备房间准备标志检测	区域范围：1794, 983, 1850, 1037

		键“segment_reset”两个为段位重置检测	区域范围：369, 221, 416, 277

		键“rites”两个为祭礼检测	区域范围：239, 615, 335, 651

		键“daily_ritual_main”两个为主页面每日任务检测	区域范围：470, 284, 507, 302

		键“exit_button_main”两个为主页面退出按钮检测	区域范围：504, 935, 569, 997

		键“disconnect_check_color_red”为红色断线重连状态检测		区域范围：1043, 350, 1113, 391

		键“disconnect_check_color_blue”为蓝色断线重连状态检测		区域范围：1043, 350, 1113, 391

		键“disconnect_check_value”为断线重连状态检测相似度

		键“disconnect_confirm”两个为断线确定按钮检测	区域范围：319, 465, 1657, 946

		键“killer_number”和键“all_killer_name”两个为检索相关参数，暂已废弃

		键“match_stage”、键“ready_stage”、键“end_stage”6个为游戏阶段判断参数	区域范围分别是：1672, 919, 1707, 952；1670, 916, 1708, 953；1753, 993, 1784, 1022

		键“ingame_icon_color”为游戏对局内状态检测参数	区域范围有两个:174, 950, 201, 977;825, 914, 1145, 965

		键“stage_judge_switch”为游戏阶段判断功能开关

	3、区域范围基于分辨率1920*1080，其他分辨率请自行换算。
		
	4、如需更改，请使用“乐玩助手9.09.exe”工具-“找色”功能自行取色。
	
	5、游戏阶段判断使得程序可以恢复因意外造成的进程错乱，但在测试中尚未表现出明显的稳定和可靠性，且只在1920*1080分辨率下工作，如果出现问题请将最后的键“stage_judge_switch”值改为0，关闭此功能。
</details>  

&ensp;●&ensp;点击`“配置”`，选择你想轮换的角色。但是 **切勿选择** 你并 **不拥有** 的角色以及 **被禁用** 的角色。  

&ensp;●&ensp;点击`“确定”`，可以保存你当前的选项。  

&ensp;●&ensp;至少选择一个角色。  

## 行为选择  

- 血 点：随机移动，以左键攻击为主。  

- 裂 隙：随机移动，规避左键，以技能为主，全屠夫技能适配。  
  - 推荐使用枯萎者，连续冲撞不求人刷血点  

★ 人类建议携带暴走族，蹲伏行动，挨刀就跑，上钩就欧。

## 快捷键  

- 快捷启动`ALT + HOME`  
- 快捷关闭`ALT + END`  

### [常见问题解答与故障排除](https://github.com/maskrs/DBD_AFK_TOOL/wiki)

### 推荐：  [黎明杀机自动血网工具](https://github.com/WKhistory/DBDAuto_BPWeb)  
