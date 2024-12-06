import re

# Texto do documento
texto = """Login: paulopim9enta - cpf :102.602.107-30 - 185.72.240.61:7097:deluxePX1:deluxePX1
Login: otavioprosper7 - cpf :546.550.485-49 - 91.123.10.54:6596:deluxePX1:deluxePX1
Login: keziasil6va - cpf :843.300.451-41 - 92.112.171.100:6068:proxysbest09:proxysbest09
Login: biavill5a - cpf :757.231.522-46 - 185.72.240.115:7151:tusky00093:tusky00093
Login: ka7tiagama - cpf :686.863.835-30 - 85.198.45.133:6057:tusky00093:tusky00093
Login: helionab4uco - cpf :524.761.395-30 - 91.123.8.178:6718:deluxePX1:deluxePX1
Login: j9oaodutra - cpf :161.636.219-72 - 92.113.245.5:5691:tusky00093:tusky00093
Login: ril6doassis - cpf :610.725.449-89 - 91.123.10.103:6645:pxflambo1:pxflambo2
Login: jaime7cruz - cpf :603.516.692-05 - 92.112.200.166:6749:deluxePX1:deluxePX1
Login: h1eliojaco - cpf :246.139.317-62 - 185.72.240.42:7078:pxflambo1:pxflambo2
Login: felipeba7hia - cpf :890.243.174-60 - 23.129.252.227:6495:deluxePX1:deluxePX1
Login: helio8valada - cpf :371.740.270-67 - 92.112.175.120:6393:tusky00093:tusky00093
Login: juliava9lente - cpf :791.835.400-16 - 85.198.47.120:6388:deluxePX1:deluxePX1
Login: regiaco0sta - cpf :822.284.573-02 - 91.123.8.41:6581:tusky00093:tusky00093
Login: guido4queiro - cpf :976.991.664-18 - 91.123.8.134:6674:proxyspeed9:proxyspeed9
Login: italoabre9u - cpf :884.372.923-36 - 91.123.8.128:6668:deluxePX1:deluxePX1
Login: fat7imasouza - cpf :133.192.436-75 - 92.112.200.143:6726:proxyspeed9:proxyspeed9
Login: anagato9 - cpf :016.800.843-21 - 23.129.252.205:6473:tusky00093:tusky00093
Login: ren4ibessa - cpf :903.414.732-00 - 185.72.242.110:5793:tusky00093:tusky00093
Login: cassiamalta1 - cpf :881.679.165-96 - 85.198.45.104:6028:tusky00093:tusky00093
Login: jan3adutra - cpf :310.809.686-95 - 91.123.10.118:6660:deluxePX1:deluxePX1
Login: gi7ldamacedo - cpf :712.107.160-62 - 85.198.47.71:6339:deluxePX1:deluxePX1
Login: lunamacha1do - cpf :794.757.727-74 - 92.113.244.169:5856:pxflambo1:pxflambo2
Login: ren2iabreu - cpf :533.567.893-33 - 23.129.254.41:6023:deluxePX1:deluxePX1
Login: maru0cezar - cpf :315.797.969-82 - 23.129.252.144:6412:deluxePX1:deluxePX1
Login: lucioprieto7 - cpf :806.965.607-71 - 91.123.10.88:6630:deluxePX1:deluxePX1
Login: lucias6aro - cpf :602.089.271-90 - 92.112.175.107:6380:tusky00093:tusky00093
Login: bi8aperes - cpf :889.072.410-23 - 185.72.242.146:5829:deluxePX1:deluxePX1
Login: enz8obraga - cpf :452.968.298-67 - 23.129.252.157:6425:deluxePX1:deluxePX1
Login: an1adias - cpf :822.811.636-52 - 85.198.47.196:6464:deluxePX1:deluxePX1
Login: heliomol9ina - cpf :565.348.101-74 - 185.72.241.104:7396:deluxePX1:deluxePX1
Login: luciaprospe5r - cpf :426.326.607-26 - 185.72.241.85:7377:tusky00093:tusky00093
Login: ninagat5o - cpf :144.043.779-32 - 85.198.47.100:6368:deluxePX1:deluxePX1
Login: net2osalles - cpf :030.443.423-09 - 91.123.8.226:6766:tusky00093:tusky00093
Login: paul4oduran - cpf :262.090.514-13 - 92.112.170.63:6032:pxflambo1:pxflambo2
Login: livianoguei1 - cpf :281.302.904-13 - 23.129.254.76:6058:deluxePX1:deluxePX1
Login: liliamacha0do - cpf :626.490.653-03 - 92.112.171.41:6009:proxysbest09:proxysbest09
Login: isaacsaro6 - cpf :434.129.340-03 - 92.112.200.3:6586:deluxePX1:deluxePX1
Login: josepir7es - cpf :699.138.916-12 - 92.113.244.89:5776:deluxePX1:deluxePX1
Login: edergat5o - cpf :684.040.294-07 - 91.123.8.87:6627:deluxePX1:deluxePX1
Login: geisaja6co - cpf :623.102.937-92 - 92.112.172.252:6524:tusky00093:tusky00093
Login: elocampo3s - cpf :256.594.109-95 - 92.112.202.101:6685:blackXP1:blackXP1
Login: estervale9 - cpf :567.441.292-87 - 92.112.202.226:6810:tusky00093:tusky00093
Login: guidom6ies - cpf :825.724.809-64 - 185.72.242.196:5879:tusky00093:tusky00093
Login: gild5arios - cpf :156.535.623-35 - 185.72.240.148:7184:tusky00093:tusky00093
Login: katia6bessa - cpf :887.645.758-53 - 185.72.240.31:7067:deluxePX1:deluxePX1
Login: cels8osaraiva - cpf :863.224.194-04 - 185.72.242.20:5703:deluxePX1:deluxePX1
Login: cassiace9zar - cpf :186.005.684-98 - 85.198.47.223:6491:deluxePX1:deluxePX1
Login: olgane3ves - cpf :192.047.211-89 - 91.123.10.62:6604:deluxePX1:deluxePX1
Login: fabiomo0naco - cpf :845.133.918-20 - 92.113.244.99:5786:deluxePX1:deluxePX1
Login: marioro0sas - cpf :151.436.774-24 - 185.72.242.27:5710:deluxePX1:deluxePX1
Login: lailalin0s - cpf :930.080.143-05 - 23.129.254.28:6010:blackXP1:blackXP1
Login: clarafreita0s - cpf :956.873.798-78 - 92.112.202.143:6727:deluxePX1:deluxePX1
Login: m2aruzanon - cpf :867.707.237-35 - 85.198.45.139:6063:pxflambo1:pxflambo2
Login: gracane7ves - cpf :969.807.940-86 - 92.113.245.211:5897:pxflambo1:pxflambo2
Login: jessyvia4na - cpf :836.160.699-80 - 185.72.240.149:7185:deluxePX1:deluxePX1
Login: re8nirocha - cpf :448.454.845-36 - 185.72.242.144:5827:deluxePX1:deluxePX1
Login: i2gorbahia - cpf :633.541.058-36 - 92.112.202.229:6813:pxflambo1:pxflambo2
Login: g6loriavargas - cpf :015.787.006-55 - 85.198.45.42:5966:tusky00093:tusky00093
Login: p8ablorangel - cpf :963.249.288-96 - 92.112.170.111:6080:pxflambo1:pxflambo2
Login: pi9eranader - cpf :666.094.507-57 - 23.129.252.43:6311:01daspx01:01daspx01
Login: esterpra2do - cpf :701.954.429-03 - 23.129.252.211:6479:tusky00093:tusky00093
Login: liam9acedo - cpf :599.973.489-40 - 185.72.240.234:7270:deluxePX1:deluxePX1
Login: cla8racardo - cpf :505.875.897-01 - 23.129.254.226:6208:deluxePX1:deluxePX1
Login: otaviomans1o - cpf :964.364.025-60 - 23.129.254.56:6038:deluxePX1:deluxePX1
Login: carlasoare1s - cpf :216.576.645-11 - 185.72.240.248:7284:tusky00093:tusky00093
Login: juliava8rela - cpf :395.194.941-46 - 185.72.241.204:7496:01daspx01:01daspx01
Login: p4ietracardo - cpf :863.288.161-20 - 92.113.244.51:5738:tusky00093:tusky00093
Login: f1abiopreto - cpf :287.058.010-01 - 92.112.172.117:6389:proxysrapidas009:proxysrapidas009
Login: o0ziellouro - cpf :020.539.191-59 - 92.112.202.9:6593:tusky00093:tusky00093
Login: ederl5ins - cpf :201.707.840-96 - 185.72.240.110:7146:pxflambo1:pxflambo2
Login: luiz5alopes - cpf :402.195.759-67 - 85.198.47.118:6386:01daspx01:01daspx01
Login: keziaque0iro - cpf :702.269.229-79 - 92.112.202.187:6771:tusky00093:tusky00093
Login: liadutra4 - cpf :817.376.955-96 - 92.112.172.233:6505:tusky00093:tusky00093
Login: l9azarofurtado - cpf :967.784.060-62 - 185.72.240.20:7056:pxflambo1:pxflambo2
Login: celsol7uz - cpf :909.910.691-29 - 92.112.175.195:6468:tusky00093:tusky00093
Login: juliazardo5 - cpf :589.396.684-80 - 185.72.240.179:7215:deluxePX1:deluxePX1
Login: den4islins - cpf :107.287.817-86 - 92.113.244.66:5753:pxflambo1:pxflambo2
Login: reb6ecaparre - cpf :767.071.125-62 - 92.112.202.161:6745:deluxePX1:deluxePX1
Login: daviterr7a - cpf :898.504.465-60 - 91.123.10.116:6658:deluxePX1:deluxePX1
Login: lazarocos6ta - cpf :249.219.503-18 - 92.112.170.180:6149:tusky00093:tusky00093
Login: laur4acruz - cpf :899.669.995-07 - 91.123.10.127:6669:pxflambo1:pxflambo2
Login: regiasoare9s - cpf :577.005.562-61 - 185.72.240.187:7223:deluxePX1:deluxePX1
Login: mair8agama - cpf :712.213.586-18 - 92.112.200.118:6701:tusky00093:tusky00093
Login: lu1cioassis - cpf :413.385.544-25 - 92.112.202.9:6593:deluxePX1:deluxePX1
Login: ninaabr0eu - cpf :501.999.576-22 - 85.198.45.55:5979:pxflambo1:pxflambo2
Login: pie6tracezar - cpf :555.447.160-99 - 92.112.170.4:5973:pxflambo1:pxflambo2
Login: biaas2sis - cpf :593.961.920-74 - 23.129.254.183:6165:pxflambo1:pxflambo2
Login: liv3iavilla - cpf :449.999.257-53 - 85.198.47.254:6522:pxflambo1:pxflambo2
Login: jessymir0a - cpf :709.941.049-01 - 92.112.170.252:6221:01daspx01:01daspx01
Login: pablofarias8 - cpf :216.866.447-10 - 185.72.242.102:5785:deluxePX1:deluxePX1
Login: guido7bessa - cpf :108.214.524-60 - 92.112.200.81:6664:deluxePX1:deluxePX1
Login: mariolou3ro - cpf :118.909.204-28 - 91.123.8.71:6611:deluxePX1:deluxePX1
Login: lai0srosas - cpf :519.054.424-91 - 91.123.8.213:6753:deluxePX1:deluxePX1
Login: n3ilogouveia - cpf :724.699.746-66 - 92.112.170.6:5975:tusky00093:tusky00093
Login: lazarojunqu6e - cpf :532.846.766-35 - 92.112.170.187:6156:pxflambo1:pxflambo2
Login: olgamel9lo - cpf :705.723.909-20 - 92.113.244.132:5819:proxysrapidas009:proxysrapidas009
Login: elizapaiva1 - cpf :766.773.936-66 - 23.129.252.72:6340:deluxePX1:deluxePX1
Login: na8tasaraiva - cpf :095.962.924-63 - 92.112.202.163:6747:pxflambo1:pxflambo2
Login: leora2ngel - cpf :912.759.560-92 - 23.129.252.187:6455:proxysrapidas009:proxysrapidas009
Login: ce5liabueno - cpf :784.860.514-01 - 185.72.241.77:7369:deluxePX1:deluxePX1
Login: elizap6rado - cpf :552.867.336-46 - 91.123.8.32:6572:deluxePX1:deluxePX1
Login: r9ejanecastro - cpf :049.591.743-58 - 91.123.8.63:6603:deluxePX1:deluxePX1
Login: italodias2 - cpf :873.621.522-80 - 91.123.10.250:6792:deluxePX1:deluxePX1
Login: milenamacedo9 - cpf :009.433.957-04 - 23.129.252.38:6306:deluxePX1:deluxePX1
Login: l7iviasaraiva - cpf :981.780.012-17 - 91.123.10.57:6599:deluxePX1:deluxePX1
Login: juliabra7ga - cpf :990.017.198-56 - 91.123.8.114:6654:deluxePX1:deluxePX1
Login: dudaramos7 - cpf :294.536.256-20 - 23.129.254.108:6090:pxflambo1:pxflambo2
Login: luizava5rgas - cpf :722.302.591-30 - 91.123.8.46:6586:01daspx01:01daspx01
Login: g2racaferro - cpf :466.010.826-00 - 92.112.202.56:6640:deluxePX1:deluxePX1
Login: mairanabuco1 - cpf :339.016.172-48 - 92.112.170.216:6185:pxflambo1:pxflambo2
Login: du4daferro - cpf :404.351.136-15 - 91.123.11.201:6467:proxysrapidas009:proxysrapidas009
Login: katia9nobrega - cpf :319.387.951-72 - 92.113.245.234:5920:proxysrapidas009:proxysrapidas009
Login: kat5iasaro - cpf :538.686.538-21 - 23.129.252.82:6350:proxysrapidas009:proxysrapidas009
Login: celial5ara - cpf :791.698.010-02 - 23.129.254.16:5998:pxflambo1:pxflambo2
Login: pablomenino7 - cpf :310.434.310-12 - 85.198.45.2:5926:pxflambo1:pxflambo2
Login: pe6drovivas - cpf :399.254.386-24 - 85.198.47.52:6320:pxflambo1:pxflambo2
Login: lucion8abuco - cpf :586.383.526-54 - 185.72.241.12:7304:pxflambo1:pxflambo2
Login: la1islara - cpf :025.243.808-66 - 91.123.10.219:6761:01daspx01:01daspx01

"""


pattern = r"(\d+\.\d+\.\d+\.\d+:\d+:\S+:\S+)"
resultados = re.findall(pattern, texto)

# Exibir os resultados
for proxy in resultados:
    print(proxy)
