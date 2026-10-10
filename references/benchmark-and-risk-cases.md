# 人工译本对照测评与首轮风险表

用于用户要求测评、建立错误表，或用现成中文译本复核难点。不要因普通短篇翻译自动生成测评报告。本表不是跨时代替换词典。

## 可重复的测评方法

1. 选能实际读取原文、邻文和有署名或出版信息的人工中文译本的单元，核实作品、阶段、文类、所选版本及节引范围。记录稳定条号、PDF页序、译者身份及未核实的版次；官网转载不自动证明其为批判版或全部措辞无误。
2. 先只看原文及必要上下文试译，记录所用技能版本；保存不可覆盖的初稿及其文件散列。参照比较必须在保存后进行。已有训练知识无法清除时如实说明；改后稿不冒充初稿。
3. 对齐实际文本单元，不只比字符串。简繁、地域译名、注号重编、译文删节、不同修订阶段分别识别。原文与参照引文范围不同，先记范围差异，再判断是否是该译本的遗漏。
4. 分开记录：确证含义误译；术语或中文表达改善；可接受异译；参照本问题；原文异文；尚未完成的核验。人工译本可以错，不能以词面相似率或多数转载作为裁决。实际修饰、先行词、限定及直接对象回到原文判断。
5. 圣经先核对文献真正引到的词句，再读思高对应经节。允许为了先做独立试译而暂时不读中文，但这时必须标作自译及经文核验未完成，后续补查；不能把未完成流程伪装成合格经文引用。
6. 依据问题修订样本，回查原文并更新适用的风险项。记录查过的范围、出现问题的独立单元数和未解项；不从有目的的小样本推算总体准确率、易错频率或无技能相比的提升。向用户区分既有人工参照、助手自查、独立模型复核与实际人工审校。
7. 需要独立代理评估时，依当前可用的 skill-creator 测评指导及授权执行；本文件本身不要求或授权每次启动代理。给评估者必要原文与输出，不预先给预期结论。新技能已吸收测试案例后，同一案例只可作回归检查，不再声称为未见测试。

## 2026-10-09 首轮实测边界

五份梵二正式文献、17个拉丁文短片段，先独立自译，再与署台湾地区主教团秘书处（UR署台湾主教团秘书处）的中文译本比较，难点参照梵蒂冈英文与思高中文经文。未发现确证的核心含义误译；发现两处中文表达可改善，另有冗词和技术表达清晰度建议，同概念用语可整理，均不计作含义错误。人工参照有四处内容或范围问题及三处文字／标点问题。这不是全文复校、统计准确率、其他语言测评或新增人工审校。未核实中文PDF具体版次及个人译者；两次模型的具体润色意见不同，不能冒称人工定论。

下表的“本轮证据”须保留；“预防风险”表示样本成功守住的区别，不是假称本轮译错。不得据此制作错误发生频率排名。候选译法只适用于相应句境。

| 检查点 | 本句候选译法／处理 | 需防止的结果 | 本轮证据与定位 |
|---|---|---|---|
| sacerdotium commune／ministeriale | 共同司祭职／职务司祭职；普通／公务亦可成立 | 用地域词差异凑错误数，或抹平两种司祭职 | 可接受异译；LG10；初稿的彼此相互可去冗词 |
| 本质与程度 | 保留本质区别及非仅程度区别 | 改成只有程度上的高低 | 预防风险，本轮未犯；LG10 |
| religiosum obsequium | 意志与理智的宗教服从 | 改成可随意忽视的私人意见，或无条件信德接受 | 预防风险，本轮未犯；LG25 |
| authentico magisterio | 权威训导；结合实际训导行为 | 只译真假鉴定意义的真实，或覆盖所有私人意见 | 预防风险，本轮未犯；LG25 |
| ex cathedra | 从宗座发言；首见可作技术说明 | 理解为坐在某座椅讲话，或所有教宗讲话 | 清晰度建议，不是确证误译；LG25 |
| Verbo incarnato及救赎主 | 降生成人的圣言，同一位基督 | 将并列称号拆成两个主体 | 预防风险，本轮未犯；LG62 |
| 受造物与救主的关系 | 不能与祂并列／相提并论 | 误作禁止任何讨论比较，而非此处的地位关系 | 预防风险，本轮未犯；LG62 |
| cultus adorationis | 钦崇礼；圣母敬礼依句义译敬礼 | 将天主与圣母／圣人的敬礼混同，或补入原文未明说的三分法 | 预防风险，本轮未犯；LG66 |
| signa sensibilia；singulis | 可感标记；按各标记特有的方式 | 把先行词从标记移为各个人 | 确证参照本指代错误；SC07，中文PDF7页 |
| validam／licitam | 有效／合法，分别保留 | 将合法与有效合并成一般合规 | 预防风险，本轮未犯；SC11 |
| 礼仪参与中的scienter／consciam | 有意识；同概念跨条一致 | 因词形不同每条另换术语；也不能与道德良心混同 | 本轮一致性改善；SC11与SC14 |
| actuose | 主动地参与；积极可按语境判断 | 只剩外在活动量，或仅以译名不同判错 | 可接受表达，建议项目统一；SC11与SC14 |
| fructuose | 富有成效／有果效地 | 误读旧译为经济实惠，删去灵性果效 | 预防风险，本轮未犯；SC11 |
| 圣传与圣经 | 圣传与圣经，相连且相通 | 把圣传降为民俗，或删去两者联系 | 预防风险，本轮未犯；DV09 |
| inspirati／hagiographi | 受默感的作者／圣经作者 | 只写一般灵感或将圣经作者误作圣人传记作者 | 预防风险，本轮未犯；DV11 |
| nostrae salutis causa所在从句 | 保留天主愿意为救恩将真理记载于圣经的关系 | 将原文关系从句删去或重排为另一命题 | 参照本从句压缩；DV11，中文PDF8页；不据此代替圣经无误论的完整论证 |
| perspiciat的中文搭配 | 为明了／为弄清 | 生成“为了解明”等词语拼接 | 本轮实际中文表达问题；DV12 |
| 使字结构与无主句 | 明确谁遵守法规、谁参与礼仪 | “使……中不仅遵守”造成主语不清 | 本轮实际中文表达改善；SC11 |
| conscientia | 良心；按道德判断语境 | 机械与礼仪的有意识合并，或写成私人喜好 | 预防风险，本轮未犯；DH02a、DH03 |
| 强制及自由的边界 | 保留免受强制、正反要求、私下／公开等维度及应有限度 | 删去限制或只保留不强迫而漏掉不阻止 | 预防风险，本轮未犯；DH02a、DH03 |
| 成义与纳入基督 | 成义；纳入基督的身体／与基督结成一体 | 将成义变成主观自认正当，将纳入误作降生 | 可接受异译；UR03a |
| Spiritus Christi | 本句为基督的圣神 | 一律将所有spiritus译为圣神或本句仅当态度 | 预防风险，本轮未犯；UR03b |
| salutis mediis及复数所指 | 救恩的媒介／工具，保留效力来源及教会与团体两类 | 无据缩成圣事、漏掉团体或变成所有团体同等完备 | 初稿可接受；参照第二句只重复教会，表达范围不完整；UR03b，中文PDF4页 |
| 真理的hierarchiam | 真理之间的次序／层级 | 改成真理真假程度或直接等同训导等级 | 预防风险，本轮未犯；UR11 |
| 文献节引路1:48–49 | 保留原文所引两节部分，不扩写完整两节 | 照抄仅保留48节的会议中文参照，或补入未引句 | 参照节引范围缩短；LG66b，中文PDF59页 |
| 弟后3:16–17及原注 | 默感、正义、善工；保留注示并说明实际底本 | 把拉丁自译冒称思高逐字引文或直接希腊译文 | 本轮自译意义可成立；DV11b，经文核验在复核阶段补做 |
| 参照本文字与标点 | 逐处检查页图及原句；有依据才修订 | 把原PDF的异常文字、错字或断句继承为自己的定稿 | 实际参照文字问题，非试译错误；LG66、SC11、DV12 |

## 可实际读取的依据

- LG：[拉丁文第10、25、62、66条](https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19641121_lumen-gentium_lt.html)；[中文PDF](https://www.vatican.va/chinese/concilio/vat-ii_lumen-gentium_zh-t.pdf)。
- SC：[拉丁文第7、11、14条](https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19631204_sacrosanctum-concilium_lt.html)；[中文PDF](https://www.vatican.va/chinese/concilio/vat-ii_sacrosanctum-concilium_zh-t.pdf)；[英文第7条](https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19631204_sacrosanctum-concilium_en.html)用于确认指代。
- DV：[拉丁文第9、11、12条](https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19651118_dei-verbum_lt.html)；[中文PDF](https://www.vatican.va/chinese/concilio/vat-ii_dei-verbum_zh-t.pdf)；[英文第11条](https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19651118_dei-verbum_en.html)用于核对从句。
- DH：[拉丁文第2、3条](https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_decl_19651207_dignitatis-humanae_lt.html)；[中文PDF](https://www.vatican.va/chinese/concilio/vat-ii_dignitatis-humanae_zh-t.pdf)。
- UR：[拉丁文第3、11条](https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_decree_19641121_unitatis-redintegratio_lt.html)；[中文PDF](https://www.vatican.va/chinese/concilio/vat-ii_unitatis-redintegratio_zh-t.pdf)。
- 经文：[路1:48–49中文栏](https://www.ccreadbible.org/chinesebible/znccb/Luke_bible_Ch_1_.html)；[弟后3:16–17中文栏](https://www.ccreadbible.org/chinesebible/zndouay/2_Timothy_bible_Ch_3_.html)。在线渠道不自动等于出版机构。

既往项目的核心误译仍见 [句法复核与纠错](translation-review.md)；不混入本轮17项的结果。
