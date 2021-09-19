#! / bin / bash
barra = "\ 033 [0m \ e [34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ━━━━━━━━━━━ \ 033 [0m "
[[! -e / bin / ipw]] && echo "/root/Panelweb.sh"> / bin / ipw && chmod + x / bin / ipw #ACCESO RAPIDO
fun_bar () {
comando [0] = "$ 1"
comando [1] = "$ 2"
 (
[[-e $ HOME / fim]] && rm $ HOME / fim
$ {comando [0]}> / dev / null 2> & 1
$ {comando [1]}> / dev / null 2> & 1
toque em $ HOME / fim
 )> / dev / null 2> & 1 &
 tput civis
echo -ne "\ 033 [1; 33mAGUARDE \ 033 [1; 37m- \ 033 [1; 33m ["
enquanto verdadeiro; Faz
   para ((i = 0; i <18; i ++)); Faz
   echo -ne "\ 033 [1; 31m #"
   dormir 0.1s
   feito
   [[-e $ HOME / fim]] && rm $ HOME / fim && break
   echo -e "\ 033 [1; 33m]"
   dormir 1s
   tput cuu1
   tput dl1
   echo -ne "\ 033 [1; 33mAGUARDE \ 033 [1; 37m- \ 033 [1; 33m ["
feito
echo -e "\ 033 [1; 33m] \ 033 [1; 37m - \ 033 [1; 32m OK! \ 033 [1; 37m"
tput cnorm
}
IP = $ (cat / etc / IP)
x = "ok"
cardápio ()
{
#PAINEL A INSTALAR
panel_v10 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v10/Painel.sh> / dev / null 2> & 1; chmod + x Painel.sh; ./Painel.sh
}
panel_v10_2 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v10_2/install.sh> / dev / null 2> & 1; chmod + x install.sh; ./install.sh
}
panel_v11 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v11/Painelv11.sh> / dev / null 2> & 1; chmod + x Painelv11.sh; ./Painelv11.sh
}
panel_v11_2 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v11_2/install> / dev / null 2> & 1; chmod + x instalar; ./instalar
}
panel_v12 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v12/install> / dev / null 2> & 1; chmod + x instalar; ./instalar
}
panel_v15 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v15/install> / dev / null 2> & 1; chmod + x instalar; ./instalar
}
panel_v15_2 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v15_2/ocspanel> / dev / null 2> & 1; chmod + x ocspanel; ./ocspanel
}
panel_v20 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v20/install> / dev / null 2> & 1; chmod 777 iinstall * && ./install*
}
panel_v20_mod () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v20_mod/install> / dev / null 2> & 1; chmod + x instalar; ./instalar
}
panel_v23 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v23/install> / dev / null 2> & 1; chmod + x instalar; ./instalar
}
panel_v23_2 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v23_2/install> / dev / null 2> & 1; chmod + x instalar; ./instalar
}
panel_v25 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v25/install> / dev / null 2> & 1; chmod + x instalar; ./instalar
}

#UPDATE VIP-VPS v23 a v25
panel_update2325 () {
wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/panel_v23_2/atu-v23-p-v25> / dev / null 2> & 1; chmod + x atu-v23-p-v25; ./atu-v23-p-v25
}

#CLEAN FOLDER
clean_folder () {
echo ""
fun_bar "apt-get update -y"
fun_bar "apt-get upgrade -y"
fun_bar "reiniciar serviço ssh"
## LIMPIA FILES
rm -rf $ HOME / install *
rm -rf $ HOME / install.sh *
rm -rf $ HOME / ocspanel *
rm -rf $ HOME / Painel.sh *
rm -rf $ HOME / Painelv11.sh *
rm -rf $ HOME / banco.sql *
rm -rf $ HOME / BD-Painel-v23.sql *
rm -rf $ HOME / sshplus.sql *
rm -rf $ HOME / bd-v15.sql *
rm -rf $ HOME / ssh.sql *
rm -rf $ HOME / plus.sql *
rm -rf $ HOME / Panelweb.sh *> / dev / null 2> & 1; wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/Panelweb.sh> / dev / null 2> & 1
echo ""
echo -e "\ 033 [1; 33m LIMPAR PASTA COM SUCESSO - \ 033 [1; 32m OK! \ 033 [1; 37m"
dormir 4s
chmod + x Panelweb.sh; ./Panelweb.sh
}

#PANIL REMOVE
remove_panel () {
Claro
echo ""
echo -e "\ 033 [1; 36m WEB DO PAINEL DESINTALAR"
echo ""
echo -ne "\ 033 [1; 37mDesinstalar MySQL [N / S]: \ 033 [1; 37m"; leia x
[[$ x = @ (n | N)]] && sair
## sudo 
apt-get purge mysql-server mysql-client mysql-common mysql-server-core- * mysql-client-core- *
rm -rf / etc / mysql / var / lib / mysql
apt-get autoremove
apt-get autoclean
reinicialização do apache2 do serviço
echo ""
echo -e "\ 033 [1; 36mPANEL ELIMINADO COM SUCESSO - \ 033 [1; 32m OK! \ 033 [1; 37m"
echo ""
dormir 4s
chmod + x Panelweb.sh; ./Panelweb.sh
}

#OPCIONES DE SISTEMA
atualizar () {
echo ""
fun_bar "apt-get update -y"
fun_bar "apt-get upgrade -y"
fun_bar "reiniciar serviço ssh"
rm -rf $ HOME / Panelweb.sh *> / dev / null 2> & 1; wget https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/SSHPLUS-MANAGER-FREE/master/Install/Panel_Web/Panelweb.sh> / dev / null 2> & 1
echo ""
echo -e "\ 033 [1; 33m ATUALIZAR COM SUCESSO - \ 033 [1; 32m OK! \ 033 [1; 37m"
dormir 4s
chmod + x Panelweb.sh; ./Panelweb.sh
}
remove_multiscripts () {
rm -rf $ HOME / Panelweb.sh * && rm -rf / bin / ipw
}

enquanto verdadeiro $ x! = "ok"
Faz
_usor = $ (printf '% -8s' "$ (free -m | awk 'NR == 2 {printf"% .2f %% ", $ 3 * 100 / $ 2}')")
_usop = $ (printf '% -1s' "$ (top -bn1 | awk '/ Cpu / {cpu =" "100 - $ 8"% "}; END {print cpu}')")
Claro
echo -e "$ barra"
echo -e "\ E [41; 1; 37mINSTALL PAINEL WEB \ 033 [1; 32m [\ 033 [1; 37m VERSAO: r001 \ 033 [1; 32m] \ E [0m"
echo -e "$ barra"
echo -e "\ 033 [1; 31m [\ 033 [1; 36m01 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL SSHPLUS WEB V10 \ 033 [1; 31m (ANT)" 
echo -e "\ 033 [1; 31m [\ 033 [1; 36m02 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL SSHPLUS WEB V10 2 \ 033 [1; 32m (DAN) " 
echo -e "\ 033 [1; 31m [\ 033 [1; 36m03 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL SSHPLUS WEB V11 \ 033 [1; 31m (ANT)" 
echo -e "\ 033 [1; 31m [\ 033 [1; 36m04 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL SSHPLUS WEB V11 2 \ 033 [1; 32m (NOVO) " 
echo -e "\ 033 [1; 31m [\ 033 [1; 36m05 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL SSHPLUS WEB V12 \ 033 [1; 32m (NOVO)" 
echo -e "\ 033 [1; 31m [\ 033 [1; 36m06 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL SSHPLUS WEB V15 \ 033 [1; 31m (ANT)" 
echo -e "\ 033 [1; 31m [\ 033 [1; 36m07 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL SSHPLUS WEB V15 2 \ 033 [1; 33m (OCS) "
echo -e "\ 033 [1; 31m [\ 033 [1; 36m08 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL SSHPLUS WEB V20 \ 033 [1; 32m (NOVO) \ 033 [1; 37m∆ "
echo -e "\ 033 [1; 31m [\ 033 [1; 36m09 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL SSHPLUS WEB V20 MOD \ 033 [1; 32m (NOVO) " 
echo -e "\ 033 [1; 31m [\ 033 [1; 36m10 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL SSHPLUS WEB V23 \ 033 [1; 32m (NOVO)" 
echo -e "\ 033 [1; 31m [\ 033 [1; 36m11 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL VIP-VPS WEB V.23 \ 033 [1; 35m (ADE) \ 033 [1; 37m∆ "
echo -e "\ 033 [1; 31m [\ 033 [1; 36m12 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPAINEL VIP-VPS WEB V.25 \ 033 [1; 35m (ADE) \ 033 [1; 37m∆ "
echo -e "$ barra"
echo -e "\ 033 [1; 31m [\ 033 [1; 36m13 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mUPDATE VIP-VPS V.23 PARA V25 \ 033 [1; 35m (ADE) \ 033 [1; 37m∆ "
echo -e "$ barra"
echo -e "\ 033 [1; 31m [\ 033 [1; 36m14 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33m PASTA LIMPA \ 033 [1; 33m (\ 033 [1; 37mINESTABLE \ 033 [1; 33m) \ 033 [1; 36m • "
echo -e "\ 033 [1; 31m [\ 033 [1; 36m15 \ 033 [1; 31m] \ 033 [1; 37m • \ 033 [1; 33mPANEL REMOVER \ 033 [1; 33m (\ 033 [1; 37mINESTABLE \ 033 [1; 33m) \ 033 [1; 36m • "
echo -e "$ barra"
echo -e "\ 033 [1; 31m [\ 033 [1; 36m16 \ 033 [1; 31m] \ 033 [1; 35m [!] \ 033 [1; 32mACTUALIZAR \ 033 [1; 31mRam: \ 033 [1 ; 37m $ _usor "
echo -e "\ 033 [1; 31m [\ 033 [1; 36m17 \ 033 [1; 31m] \ 033 [1; 35m [!] \ 033 [1; 31mDESINSTALAR \ 033 [1; 35m [\ 033 [1 ; 37m IPW \ 033 [1; 35m] \ 033 [1; 31mNúcleo: \ 033 [1; 37m $ _usop "
echo -e "\ 033 [1; 31m [\ 033 [1; 36m00 \ 033 [1; 31m] \ 033 [1; 37mSALIR \ 033 [1; 32m <\ 033 [1; 33m <\ 033 [1; 31m] <\ 033 [1; 37m @ admmanagerfree \ 033 [0m \ 033 [0m "
echo -e "$ barra"
echo -ne "\ 033 [1; 32mOQUE DESEJA FAZER \ 033 [1; 33m? \ 033 [1; 31m? \ 033 [1; 37m:"; leia x

caso "$ x" em 
1 01)
Claro
panel_v10
saída;
;;
2 | 02)
Claro
panel_v10_2
saída;
;;
3 | 03)
Claro
panel_v11
saída;
;;
4 04)
Claro
panel_v11_2
saída;
;;      
5 | 05)
Claro
panel_v12
saída;
;;
6 06)
Claro
panel_v15
saída;
;; 
7 07)
Claro
panel_v15_2
saída;
;;
8 08)
Claro
panel_v20
saída;
;;     
9 09)
Claro
panel_v20_mod
saída;
;;
10)
Claro
panel_v23
saída;
;;
11)
Claro
panel_v23_2
saída;
;;
12)
Claro
panel_v25
saída;
;;     
13)
Claro
panel_update2325
saída;
;;
14)
Claro
limpar_pasta
saída;
;;
15)
Claro
remove_panel
saída;
;;
16)
Claro
atualizar
saída;
;;
17)
Claro
remove_multiscripts
saída;
;;
0 | 00)
echo -e "\ 033 [1; 31mSaindo ... \ 033 [0m"
dormir 2
Claro
saída;
;;
*)
echo -e "\ n \ 033 [1; 31mOpcao invalida! \ 033 [0m"
esac
feito
}
cardápio
#fim
