program exs21;

uses crt;

var codE,codC: integer;
var peso,novoPeso: real;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ('caro usuario este programa programa lhe mostrara de acordo com os dados que voce inserir, o peso da carga do caminhao.');
 writeln ('o preco da carga do caminhao, o valor do imposto do estado, e o valor do produto acrescido do imposto.');
 writeln (' ');
 write ('para inciar tecle enter.');
 readkey;

 //voc ler do usuario dois codigos que sero utilizados na estrutura case e um valor que  o peso da carga em toneladas.

 clrscr;
 writeln ('primeiramente digite o codigo do estado de origem, de 1 a 5.');
 readln (codE);

 clrscr;
 writeln ('agora digite o codigo da carga, de 10 a 40.');
 readln (codC);

 clrscr;
 writeln ('agora digite o peso da carga em toneladas.');
 readln (peso);

 novoPeso:= peso*1000;

 //se transforma o peso em toneladas em quilos e se comea as estruturas case.

 clrscr;

 {a estrutura primaria  a que tem como condio o codigo de estado que definira o imposto.
 a estrutura secundaria que entra dentro de todas as primarias  a que tem como condio o codigo do produto que definir o seu preo.
 ento se faz os calculos para cada estrutura considerando o valor de imposto, e o preo de cada quilo de produto.
 e se apresenta ao usuario esses resultados.}

 case codE of

   1: case codC of
      10..20: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 100):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 100) *0.35):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 100) *1.35):4:2, ' .');
              end;

      21..30: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 250):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 250) *0.35):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 250) *1.35):4:2, ' .');
              end;

      31..40: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 340):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 340) *0.35):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 340) *1.35):4:2, ' .');
              end;
      end;

   2: case codC of
      10..20: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 100):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 100) *0.25):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 100) *1.25):4:2, ' .');
              end;

      21..30: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 250):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 250) *0.25):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 250) *1.25):4:2, ' .');
              end;

      31..40: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 340):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 340) *0.25):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 340) *1.25):4:2, ' .');
              end;
      end;


   3: case codC of
      10..20: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 100):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 100) *0.15):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 100) *1.15):4:2, ' .');
              end;

      21..30: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 250):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 250) *0.15):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 250) *1.15):4:2, ' .');
              end;

      31..40: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 340):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 340) *0.15):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 340) *1.15):4:2, ' .');
              end;
      end;

   4: case codC of
      10..20: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 100):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 100) *0.05):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 100) *1.05):4:2, ' .');
              end;

      21..30: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 250):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 250) *0.05):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 250) *1.05):4:2, ' .');
              end;

      31..40: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 340):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 340) *0.05):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 340) *1.05):4:2, ' .');
              end;
      end;

   5: case codC of
      10..20: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 100):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 100) *0.0):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 100) *1.00):4:2, ' .');
              end;

      21..30: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 250):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 250) *0.00):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 250) *1.00):4:2, ' .');
              end;

      31..40: begin
              writeln ('o peso da carga em quilos e ', novoPeso:4:2, ' .');
              writeln ('o preco da carga e ', (novoPeso * 340):4:2, ' .');
              writeln ('o preco do imposto e ', ((novoPeso * 340) *0.00):4:2, ' .');
              writeln ('o valor da carga com imposto e ', ((novoPeso * 340) *1.00):4:2, ' .');
              end;
      end;

 end;

 writeln (' ');
 write ('para encerrar o programa precione qualquer tecla.');
 readkey;

end.
