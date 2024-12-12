"""
--- Day 3: Mull It Over ---
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

Your puzzle answer was 161085926.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""
import re

def main():
    data = """
    select(){,(where()+-mul(514,727);:]]what():^*from(764,547) mul(550,305)$^^%>select(587,376)mul(94,564)select()when(633,175)<where()mul(260,379)mul(790,810)&!$%mul(557,683) why(){/mul(220,10)!+{+mul(654,746){who()what() !%mul(89,191)who()select()*#&>[[mul(302,490)$-}&**+mul(335,535)@select()>select()mul(241,166)when(800,629)mul(758,530)',^ &!~%/#mul(938,70)?&!from();mul(412,287)}/mul(230,620)(~select()what()select()'@mul(410,577)$mul(720,516)-mul(373,78)when()!^:@{)mul(793,973)who()when()mul(85,246)>what()}[#[@!^/mul(396,22)@when()-;:':>}mul(515,670)<[mul(38,415)?~<?mul(200,147):mul(328,235)*<what() (] ::what()mul(571,33)mul(679,122)>select()why()^when()*#+($do()']select()>:^/when()^mul(440,923)<what():mul(971,274)(mul(833,181))don't()why();{#mul(468,401)$+?mul(446,956)where()mul(391,995)who(813,746),^who()%how()^when()mul(284,629);[why()mul(922,806)%}mul(183,352)where() [{,why(475,275)mul(547,62)$mul(753,602)*!%where()-mul(956,732)$;what()<;'{:*mul(481,556)from()*{select():what()'#mul(905,420)what()mul(327,771), who()}mul(45,757)mul(366,653)where(459,755))don't();when()mul(807,855)where()$)>@mul(48,816)mul(370,665)@*>who()^,when()mul(155,426) mul(132,914)^%select()&when()/from()(+}mul(296,176)mul(361,479)%{;!,'who()where():mul(506,495)#who()&%< ^mul(481,87))&!;mul(541,563)%don't(){}'-),from()$mul(495,427)^when()mul(640,499)select()}:] )%+()mul(967,918)?when()select()<{/who()what()mul(505,225)(mul(90,482)>!from()when()#do()mul(620,841):who()!mul(719,850)where()-)mul(931,185)?;select()]@,why()%]mul(39,103)mul(687,103)$%];how(337,314)[}$-when()mul(282,494):;!where(188,779);who()mul(342,554)<^who()(why()where()who(345,491)%mul(407,74)why()&}'%'mul(324,781)mul(90,925):from()mul(828,16)mul(438,549){what()>$why()*what(35,607)mulwho()mul(91,548)>,what()select()]&how()@mul(384,93!select(),where()$mul(835,662)@{don't():#<^/-+mul(489,462)>>where(){why()where()---when()mul(53,461)/~?mul(273,777)mul(119,879)+@'when()-mul(585,949)?['when()from(946,632)mul(22,105)>-:how())from();mul(439,876)?mulwho()@who()when()<@{-mul(111,687)$&mul(432,628)%*,{when()mul(287,508)'-select()}don't()/#~-@from()[:#mul(111,655)%: &;mul(518,391)don't()<from()%-~-!@mul(301,138)(,how()mul(654,521)!*when()--({who()how()don't() ~where()!~mul(910,877)?+select()+-[#&do()*< +-what()&how()%$mul(123,641)*?&mul(488,741)<}@@&?what()how()what())mul(301,649);why()%mul(259,148)$~')&[{mul(83,94)~select()~^when()mul(232,572)mul(889,281)why()%*#$}<[mul(256,607)}({mul(382,953)what()how()why() who()from()!?%mul(433,147)+>&mul(197,749)@who()*mul(935,21)+> who()why()mul(299,881)who()]@+%/from()[?do();{+[why()$select()#mul(264,731)]'select()what();+who()mul(713,161)where(931,649))mul(360,529)}where()!;]how()<mul;$-:]]how()#where()select()when()mul(971,836)when():[how(){mul(567,429)!}{{',mul(522,696),why(){mul(833;#-&#,select()~mul(80,121)+*,#how()select()${>how()mul(619,728)how()<%}+}mul(420,324);{!from();mul;)>mul(144,181)who()}?~where():who()${ mul(261,691),why() /+mul(189,450)
+when()%^]]/when()~@mul(533,22)mul(231,586)mul(107,724)!@mul(504who()@}when(291,528)mul(691,859)/}#mul(726,544)from()[>>what()^<mul(316,707)@&why(),what()mul(798,459) why()~)]mul(612,148)[??when()]*~mul(634,978)mul(477,947)<?(&!;what(724,289)@~^do()who()mul(828,259)mul(595,267)who(671,135)}why()&how()mul(351,552)when()how()^>?^from(762,977)mul(67,280)(who()^mul(586,844)}how()<from()mul(521,525)'select()mul(379,96), mul(478,481)where(465,218)mul-&*: ~mul(123,281)when()mul(249,626) <}mul(190,620)mul(21,142):from(278,629)}how(997,873)when()'from()#mul(117,186)^:]when(128,617)mul(940,708);mul(960,867);[,~when()when() mul(135,71)where(972,23)mul(79,533)how()* )%<&do()@>how()+where(),mul(886,320)#from(691,802)mul(376,296)'why()[@}how()#why(530,714)?>mul(791,363)?what()$${@why()>+mul(133,626))why()&}what(){%(mul(474,459)what()where()(^mul(311,372)mul(243,118)where()@mul(302,760):{who()-'{+mul(145,293)}why();how());$]mul(652,761%? ;]:@mul(259,51)@<mul(369,322 +#!mul(99,991):from()/}mul(137,230)why()}^%^{}select()where()mul(226,287)mul(590,394)[>>'mul(474,995){don't():}*mul(309,511)?select();(mul(553,164)]how(){when()mul(556,560/~when(464,361),^<#[/&do()when()&who()<mul(618,347)]/what()&mul(210,454)@,'^/%who()mul(297,766)who()&:{mul(961,326))&:#')what(663,984)mul(340,326)mul(329,543)%^#/{!mul(28,451)}@@mul(428,233)^%<-how()mul(710,863)[mul(944,973)[where()~[]where()'%~why()don't()!,@#%mul(582,87)$[[@ mul(569,58),]mul(746,840)[(mul(74,146)'where()(#+;mul(517,818)mul?*[->*mul(22,727)from()):who()when()}mul(367,34/when()where()mul(226,816)mul(421,33'(,(#, <who())what()mul(247,12)+when(199,246)who()what(912,935)~?select()how()&how()mul(620,264))how(726,381)/!mul(586,607)#when()[mul(684,722)&%-from()mul(11,63)&where()<select()^)<%select(127,191)mul(662,331)}% mul(631,2)~]mul(987,288)mul(261,47)]{when()>?who()do()%;+-<what()#*+mul@]@?[^mul(650,139)<who()[#don't())}-from()?:who()[mul(561,710){~+how()don't()mul(788,270)mul(151,849)+{;%[#~mul(531,530)how()>:-mul(99,868)#{[why()who(504,690)?mul(119,337)+,mul(250,122))%#%mul(708,536)>select();from()mul(480,332)}&what(423,278)mul(891,459)}mul(852,128)mul(418,844)~select()[{when()(mul(69,312);!)where(419,852)<:*@-don't()what()!$-;{mul(91,636)-when()select()~from()(&mul(894,19)how()]@,[do()#,what()'@mul(116,57)why()from(),@-?mul(651,74)]what(704,54)how()<$mul(169,494) )from()$~-mul(44,491)$mul(29,368)'why()+-+mul(961,385)>who()select(137,499)mul(586,30)$%when(765,538)?why()(mul(378,568)}select()[:[%?$from()don't();mul(375,803)#']/@/^}*where(184,703)mul(21,508)>;+,mul(921,355)};mul(594,553@<?when()what()%%when()*don't()-<,from(342,971))mul(983,69!!!mul(980,691)why()mul(200,735)select(435,520){?mul(489,554?~!mul(212,991)/#<$!<*mul(751,323)mul(102,317)when()},^;why()mul(51,80)}+what()$~[mul(454,897)'/);(>%])mul(793,439)]from(599,582)mul(982,538)}//^;how()~)'from()don't()~&who()<+#+mul(386,116)>/~who()mul(373,106)+#!do()(&-select(),+~;~mul(59,223)mul(233,653)mul(547,404)?where()~%don't()}}select() from()@] from()mul(150,196) ]}(>mul(514,824)where()+mul(332,418)
/>'^')what()mul(590,783)?$when()mul(55,422)from()~]select(198,113)from():}don't()mul(436,985)^:select()from()@//don't()/mul(675,976)$from(),!&]#*&don't()*[#how()~/*mul(172,297)<-{,select()};mul(866,305)$mul(938,509)+>mul(100,651)%where()how(223,719)/){!!;(mul(163,66)+''when()mul(217,127)^},(why()how()what()]who()mul(39,897)>/(mul(966,889)-]'}{,<mul(488,570)$@select(){do()~$@mul(878,77)why()-^mul(670,359)-]select()#{:}[mul(56,569);do()}}what()why()/what()[$mul(614,976)when()who()^'where()(mul(852,588)who(){how()}@when() $mul(532,868)}mul(603,823)#>+,!$$<mul(517,713)/&(select():where(910,84)[select()mul 'select(899,120)from()from()>why()from()mul(338,824)where()/&;mul(230,684)@'where(354,854)- )%when()mul(288,730){from()){}where()mul(124^}'(&don't()mul(688,399)from()++[how()why()mul(136,861who()!?#select()!]where()!do()&how()where()when()mul(968,380)'-$select()why()&:;mul(906>select()^~who())>:*mul(433,704)&why()#who()%@;what()>;mul(848,947) from(497,742)?select()~mul(590,692)why()* ,(<<)where()*mul(102,487)when()]where()>*when()!mul(406,710)mul(962,153)who()who()what()+&from()mul(419,854)$/mul(201,493)from()-)select()'^:[!;mul(779,883)why()why()}?why()(don't()what()]%~{mul(966,261)how()[when())^when()]mul(513,694)/*:when()select()who()'mul$?++~?:$mul(657,498)$ &why()mul(310,762)^+what()~,what()why()why()#}mul(320,448)%mul(886,159)(]what()?'@why():[mul(415@who()$what(){select()who())mul(912,558)select()<mul(614,536)don't()!%{mul(224,83)#why()who()where()+$mul(266,718)[where(437,374)?+who()};<+mul(939,819)'$mul(24,251))mul(101select()why(){how()when(),%mul(86,947)[<}^()%where(526,396)mul(694,25)^;do()what(); (how(307,882)mul(285,650)*%who()[#{what())/~mul(95,593)where()who(){/when()why()mul(931,886)&mul(110,763)}>where()%'why():mul(784,109)-&:-]mul(354,211):*#~mul(637,881),$from()mul(947,709)what():,'mul(284,267)&from()mul(259,860)/^],&(when()when()^mul@select() how()!mul(462,151)~,)where()mul(7,166)**what()<~<do()who()(how())why()}@[([mul(478,668)+!how()mul(118,569)^&;when()-@ mul(181,739^who(432,515)$mul(105,134)where()<from(880,223)who()select()%]mul(489{&>mul(137,598)^]~>mul(561,283)*@ ;select()mul(262,658)who()<,-what()/-why()mul'$;;-]<mul(7,931)?& ^+)where()mul(345,667)/^'mul(3,959)@%when()mul(522,907)~~  ]&%*how(106,70)mul(986,967)!where()when()mul(754,736)where(515,293)why()how()-:!mul(750,438)why()/~ mul[@'['>#why()>mul(510,757)$what()who()>mul(139,401)where()^#&/*mul(332,919)>?how()]when()/mul(218,127)[+mul(504,583)why()$>^mul(649,222)@?don't()from()&what())&'^mul(878,444),,mul(340,684)when()'why()when()?why()mul(852,617)mul(569,36)~(select():>~&/when()@do()<why(444,49)[#[?##^mul(298,203)([why()?,++:}mul(263,671),mul(197,758),';mul(893,114)who()^(,(#why()[*mul(917what()select()[where()from()&'@ [:don't()'+ ($]<where()*{mul(269,55)from()%!select()how()who()where()@mul(81,174)from())^who()mul(872,888&when()>why()from()>who()where()mul(93,146)(;why(863,117)mul(681,428);#mul)$from()how())?{] mul(793,537)where() @~?++?when()why()mul(163,958)select()}who()mul(540,501)$when()#who()/mul(331,537)[>~why()what(395,317)[)[mul(928,496):mul(127,943)$>mul(18,669)?&mul(443,860)when()!;;&select()*mul(624,669)[}:,*>]mul(941,338)?%where()((how();<~when()mul(483,529){)/'+'~$mul(254,159)when():when()'*!??%mul(731,125)when(670,595)]^^from()'?]mul(912,606) ):[^do()#{;?-mul(851,526)>'!'mul(689,174) >?{)how()/;what()mul(919,455)]mul(320,219){#+) {mul(267,831)((from()&:[-from()mul(84,102)mul(291,186)/+}*mulhow()?who()-*mul(973,390)
 (~{$where()why(250,398)/how()&#!/usr/bin/perlwhy()-{{#^%>mul(772,422) 'how()}&)mul(184,89)$<how()what()%*~mul(197,267)*)[^mul(703,592)when(), ;why()select(151,652){{>what()mul(376,816)when(),@#mul(949,642)'/+select() [mul(399,146)[~who(){;~ mul(526,131)when()mul(787,620)@~+?from()@-mul(310,482)}:$?what() ,mul(360,720)/why()why()#)^mul(561,462)+@:-{who()mul(403,894)from(),}{(('?!mul(555,514)?-:#&]$-mul(18,725)??mul(901,195)how()mul(814,623)$;~)select()/mul(4,986)#,{-]{!*~mul(833,296)/?mul(496,21why():@/#[what();mul(162,231))>~do()select();+*^?}?mul(38,18)?*who()&why()/who(479,558)from()%,mul(225,613)mul(494,841)'who()%@+{>&~mul(586,498) select()*!/]};<mul(818,498)(}#@+mul(795,500)mul(285,406);;:  ,mul(404,65)]] ;!when()+what()''mul(201,457how()%mul(489,759)!who():where()?mul(381,280when()mul(312,151)who()^-mul(236who();who();(&?&]&]mul(393,302)&>-; /what()where()mul(614,161){select()where()+!what()/-mul(927,228)mul(432,16)when()?&+'^mul(539,745)]^when()what()mul(970,413)+<&:don't()$%mul(533,997))-mul(574,681)mul(978,225)&![who()why()(>mul(453,460)why()*+how()~!why()where()*-mul(840,804)>+mul(570,880)/>how()'-~*;+mul(367,248)$@what()mul(303,242)when()?>!!!-what()>%mul(547,184);when(300,185),^mul(196,377)~<{,[@from()when()from()'mul(727,421)>mul(199,873)],select()-+<&where()mul(962,772):what()/[${how()<*where()mul(534,770)select()/how()>*mul(356,156)((%where()}~how()#who()mul(801,644)from()mul#select(458,914)how()where()~}(}what()mul(273,584)who()mul(692,224)(>what()where();%,-mul(779,81)<[~who()!mul(786,30)]':mul(328,225)/when()#])(>:?:don't())*/mul(914,292)why()mul(83,290)[~mul(257,792),;+]*mul(949,612)*{;[-:]$^]mul(813,824)]/mul(5,572)}+don't():)from()*[>+(#who(422,860)mul(243,781)<-mul#<*<#&{?/'mul(579,115)(:mul(861,206)?)<why()how()why()when()/&mul(919?''/?',mul(859,273) '/&~why()[who()]/mul(865,638)-<$(when(534,151)what()mul(756,102)''<% ]mul(521,726)how()*;*-~'~mul(830,632)><&{>;mul(331,573)mul,^->,~>?who():<mul(294,77)/,:/}},mul(477/who()what()@<}why()mul(113,420)?+,mul?why()(*+[>from()mul(463,386)['{*>],when()?mul(740,88)]<[where()from()-]mul(685,334)+how()}how()^mul(973,106)select()$+mul(867,634)do()@-?mul(535,483)how()$<mul(478,385))[#&mul$@/select()#$[}:#]mul(965,153)why(110,391))}how()mul(484,578)who()-<mul(847,771)/mul(921,939), ~when()%mul(981,816)$[how()$*who(578,752)>[mul(161,41)]where(),#,mul(129,507)don't()who()what()<how()mul(554,49)(^:mul(618,748)$%<:<> mul(214,987)[ *^*[&mul(870,285)when()how())(+)+who()^<mul(581,483)]mul(921,982:]*%how()<mul(434,655):+mul(242,610)mul(614,631)what())where()how()what(932,531)what()where()}why()%mul(494[<;what()% %how()+mul(357,150)who()?mul(949,239)mul(802,54)where()!where()*?+/mul(209,916)&&&select()mul(637,422)-,~why()?)where()^mul(502,914)(how(913,389)^how()what()what()@ from(382,173)where()mul(860,112)/don't()'['#when()mul(110,847-mul(828,62)mul(370,262)@[!][^#why()@mul(693,119)who()$what()$&mul(399,511)from()}-who()(when() *do(),&*(#}mul(395,383)why()how()>how()how()'why(990,834)<@from(535,913)mul(741,712)why()when()who()@>-*!mul(296,759)$@where()mul(585,923)where()who()/why()]}>mul(163,233) ;;what(771,674)when()mul(553,949)select()when()'mul(545,530)
( !>{!-*}mul(646,888)]-?<mul(908,145)mul(872,423)<why(523,766)$;what() &mul(724,993)]}from();>why()+mul(359,478)why()mul(186,893)]where()what()when() >select()mul(592,52)where()select()from()[select()from():~'/mul(164,308)what():>^)why()how()$&who()mul(377,499)why()((where()@~who(),mul(658,47)#how()+%from()'/select(287,448)]~mul(759,688)!<?%;}*mul(623,353)&#;~{mul(830,695)do()mul(755,160)-?{mul(138,691)mul(161,105)do())*&:who(592,695)![/mul(542,698)why()%/*do()[$from()~[mul(274,212)>@?]{(~mul(196,596)who()+mul(759,422)/@[#>where()mul)-how()>$&:$@},mul(861,458))mul(126,262)@;<how()(mul(986,49<)^[///[mul(615,656)-}): when()/mul(266,494)/)who()who()>what(){};:don't()#mul(695,332)>what(),why()#++%select(){mul(471,679)^select()/mul(387,568)when()%(]*how()>do()' ^]?mul(777,56)>where()(why()select(14,295)mul(874,481)!from(){;~how()@mul(22,505))~who())when():&mul(395,566)-(~what(231,98)$$;$mul(326,815)>from() select()^who()#mul(189,720)what(),from()don't()>%+/mul(418,532)-;):<when()[<%mul(561,959)/<*~/{mul(518,185)? ,select() <do()who()who()select()from():where()?when()mul(327,206)mul(501,728)',what(675,175):from();what()/{:don't()mul(219,962)when()'mul(7,809)/$;mul(768,798)mul(353,892)?from()! when()what()->don't())@:#<mul(899when()*;}^ &mul(506,552)mul(703,677):#}mul(13;when()don't()&/+><from()what()-{mul(801,431)(/mul(330,809)>!when():$[:<['mul(764,131)$:@&[from()%+~ mul(258,284)from(810,941)&how(232,473)mul(338,578);/select():mul(990,919)from()how()>[{!}mul(69,711),when()+do()}/[#who()*mul(907,255)?!}{]*mul(781,224)#select()<mul(400,377)mul(224,640)/@{why()mul(97,222)'~:select()mul(723,191)<~how()&->mul(755,122))<why()^]why()]mul(348,579)]where(758,732)mul(939,550)^]when()what()@*{don't()'+/:how()]}@@mul(21,125)mul(138,133)mul(482,114)where(),from(),*from()!/;[don't()why()what()how()mul(732,224)?!#?***!mul(823,749)%#/@*<what()mul(980,685)!;:/~} <$mul(51,373)$-!who()mul(523,713)!)~{%mul(16?;[who()!$how()&how()mul(461,976)#mul(108,138)when()@'}   ;(;mul(194,793)~%' ?from()select()[when()mul(79,491$*#%:mul(914,754)$' where()$who(){why()mul(692,138)+;*}mul(853,262)why()$mul(15,398why()*>-:[',mul(863,596):how() who()%select()select()[what()do()+where()^+mul(722,58)^[,how()?#^ !:mul}&select()~{}mul(885,728)when()?mul(468,630)?where()from()select()>*~:don't()%#}$@-)mul(200,579)why() mul(10,435):)/;@{;mul(298,190)where()why()$ mul(9,631);where(7,826)@-don't():':;[,!@+mul(273,471)mul(325,690)mul(267,174)mul(339,952)}what()>)>@mul(307,862)do()why(335,510)]&>( mul(636,749)(-mul(592,773)!mul(2,50+'#mul(338,514)#;why()where()mul(127,711)@mul(146,911)mul(860,601)%select()mul(806,306)mul(410,847),:[mul(73,481)+don't()>}<what()mul(826,657<+ {*^? what()mul(172,949){'~+#mul(732,513)how()'/why()*+/#&)mul(11,422)+'%@+when()$why(383,170)how()mul(190,688)]!{select();who()what()mul(450,687)from()what()mul(171,95)how()how()where()mul(631,790)~how() @$why())[mul(893,598)mul(39,888)#([/what()!]*}mul(290,685)!#who()[$do()^+@what());{$mul(463,742):$mul(118,146)@mul(39,34)what() <,when()@@mul(489,439)mul(874,442)how()~where()^who()select()-don't()/:how();when():$)mul(975,618)why()mul(732,833)where()mul(17,484)
(>&)]mul(509,882)*/@~*<!&mul(813,280)::$+-*^mul(741,365)]()what()from(804,684)mul(734,644)*<]]%who()}[^don't()when()!;)mul(55,766+!select(797,794)@where()mul(595,285)why(807,706)/when(298,410)what()select()mul(439,186):mul(976,645)>where()-!mul)$do()where()?mul(308,113)/@?why()<where(35,826)&mul(127,972)^%<~??[!%;mul(781,845)/?#(select()mul(949,130)#{-#,mul(612,396)*{@@%'/mul(343,689)>where()>%mul(970,425)~[$@'[mul(83,136)+<%who()who()who()^~where()mul(960,152)when()mul(714,401)how()?]from()*!what(313,652)mul(455,389)select()why()<-[)%:(%mul(929,53[-@%~;%]where()why()mul(293,806)from(258,940)[mul(959,603)!@)why()?{{$mul(744,798) '{}&<&?,mul(389,91)#'select()@,who()/$<mul'who()where(634,260)^*$mul(625,376)@what()&mul(7,35)#)?!how(714,530)don't()from()who()>($-@,mul(792,652)how()mul&)!do())-}?~select()>mul(527,656)mul(220,657)who(453,708)mul&when()/when()+ how()how()%%@mul(62,191)'{%,mul(13,233)mul(780,237){from(817,212) when()mul(216,970)@what()}<: - ;mul(954,521)+mul(645,579)mul(695,53)%{},mul(927,488)$/$$what()&what()mul(815,350)](select(){;mul(650,656)&<:what(70,971)* mul(452,286)select()#&)when()+mul(438,390)>what()/mul(353,213) &from()~mul(920,652)~mul(971,287)don't()select()}/mul(4,595)where()-mul(332,353);>+mul(64,192)mul(33,846)}'where()(:mul(13,41)[@!^][(^$mul(728,587)what()>^&what()>who(73,62)why()where()mul(501,624)(%!mul(187,871),;>from()(, mul(563,884)]]/[who()mul(685,629){where()from()@@',who()why()<mul(741,377)'+{+'$+^/mul(69,647)!-mul(338,68)!why()mul(752,772)-'from()'what(){[&-mul(193,86)don't()from(899,805)how()what()+'+^mul(492,628)};from()*when()#?select()mul(20,602))-:where()mul(34,881),how()}mul(777,504){;mul(425,245):how()</:&}%mul(504,651)mul(193,8)+&who()+!^*{mul(247,144)}[#;when()where()mul(857,787); % (>;mul(57,598)mul(799,387)why()?mul(963,99)*-!''when()mul(606,12)who()]how(), mul(615,921)/what()from(858,351){how()#who()@mul(379,934)~/{mul(871,792)<[+&mul(206,542)mul(154,161)-when():why()[mul(663,226)>from()from()?#mul(320,293)>select()!@;from()where()<^~mul(865,92)mul(834,118)select()#>mul(36,886) why()[>,,))select()mul(777,447)what()};<>how()from()*mul(942,312)how()]mul(810,261)select()@+>)'){mul(356,987){mul(33,198)[select()from()where()({mul(752,594)$why()who()>,?^where()->mul(478,705)why();select()from()when();]/]from()mul(878,617)@who()<how()%;mul(951,929)<& ~mul(193,497) (mul(670,912)&from()*from(57,764)mul(872,457)]mul(411,192)@from(247,487)@*'select()mul(830,878)when()<?@!~why()mul(103,203)([- ;who(37,653)who()+{mul(574,907)$mul(288,478)'who()@select(453,494);-where()why()#mul(418,593)+^%>-who()[&&mul(554,90)#+:^do(), <{mul(978,459)/##[^ ]how(); mul(470,763)mul(342,6):&mul(192,104)from(220,224)[mul(309,253)$}mul(98,92)[mul(690,632)how()why()!>@mul(880,975)~/<what()}mul(233,433),>what()why()/*[mul(663,3)when()[@! )&,~^mul(965,150)#~},%^(]from()mul(503,640)::where()mul(146,66)&)~[mul(37,741)mul(714,547)/;
    """
    solve(data)

def solve(data):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    matches = re.finditer(mul_pattern, data)
    mul_matches = []
    for match in matches:
        mul_matches.append([match.start(), match.groups()])
    print(mul_matches)

    dont_matches = re.finditer(dont_pattern, data)
    dont_positions = []
    for dont in dont_matches:
        dont_positions.append(dont.start())
    print("dont: ", dont_positions)

    do_matches = re.finditer(do_pattern, data)
    do_positions = []
    for do in do_matches:
        do_positions.append(do.start())
    print("  do: ", do_positions)

    
    enabled = True
    total_sum = 0

    for i, (x, y) in mul_matches:
        while do_positions and do_positions[0] < i:
            enabled = True
            do_positions.pop(0)
        while dont_positions and dont_positions[0] < i:
            enabled = False
            dont_positions.pop(0)
        
        if enabled:
            total_sum += int(x) * int(y)
    print(total_sum)

main()
