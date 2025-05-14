program exs23;

uses crt;

var horas, grat : integer;
    peri,cat: char;
    salMin, salLiq, valHora, salBruto, auxilio, imp : real;

begin;

 {depois de se declarar as variaveis, se apresenta o programa ao usuario.}

 clrscr;
 writeln ('caro usuario te calculara e te mostrara, o valor da hora em funcao do periodo trabalhado, o valor do salario bruto,');
 writeln ('o valor do imposto, sua gratificacao, o auxilio alimentacao, o salario liquido e sua classificacao.');
 write ('para prosseguir tecle enter.');
 readkey;

 clrscr;
 writeln ('por favor digite o valor do salario minimo.');
 readln (salMin);

 clrscr;
 writeln ('agora digite a quantidade de horas trabalhadas.');
 readln (horas);

 clrscr;
 writeln ('agora digite o periodo que voce trabalha sendo M=matutino, V=vespertino, N=noturno. Lembre-se de colocar letra maiuscula.');
 readln (peri);

 clrscr;
 writeln ('agora digite sua funcao O=operario, G=gerente. Lembre-se de colocar letra maiuscula.');
 readln (cat);

 {ento se le as variaveis do salario minimo, da quantidade de horas, do periodo em que o usuario trabalha e de sua
  funo, para que se possa realizar os calculos.}

 clrscr;

 //a primeira cadeia de ifs  para definir o valor de cada hora trabalhada.

 if (peri='M') then
    begin
    valHora:= salMin*0.10;
    end

    else if (peri='V') then
            begin
            valHora:= salMin*0.15;
            end

            else if (peri='N') then
                    begin
                    valHora:= salMin*0.12;
                    end;

 salBruto:= valHora*horas;

 //ento se abre uma estrutura de case com uma cadeia de ifs interna para se calcular o valor do imposto.

 case cat of

     'O': begin if (salBruto >= 300) then
                 begin
                 imp:= salBruto*0.05;
                 end

                 else if (salBruto < 300) then
                         begin
                         imp:= salBruto*0.03;
                         end;
        end;

     'G': begin if (salBruto >= 400) then
                 begin
                 imp:= salBruto*0.06;
                 end

                 else if (salBruto < 400) then
                         begin
                         imp:= salBruto*0.04;
                         end;
        end;
 end;

 //ento se abre outra cadeia de ifs para se definir de quanto ser a gratificao do usuario.

 if (peri='N') and (horas > 80) then
     begin
     grat:= 50;
     end

     else  begin
           grat:= 30;
           end;

 //ento outra cadeia de ifs  aberta para definir de quanto ser o auxilio alimentao do usuario.

 if (cat = 'O') or (valHora <= 25) then
    begin
    auxilio:= salBruto/3;
    end

    else   begin
           auxilio:= salBruto/2;
           end;

 //se calcula o valor do salario liquido para apresentar ao usuario.

 salLiq:= salBruto - imp + grat + auxilio;

 //ento ja na ultima cadeia de ifs se apresenta ao usuario todos os resultados juntamente com sua classificao.

 if (salLiq > 600) then
    begin
    writeln ('o valor de cada hora trabalhada e de ', valHora:4:2 , ' .');
    writeln ('o valor do salario bruto e de ', salBruto:4:2 , ' .');
    writeln ('o valor de imposto pago e de ', imp:4:2 , ' .');
    writeln ('a gratificacao recebida e de ', grat , ' .');
    writeln ('o valor do auxilio alimentacao e de ', auxilio:4:2 , ' .');
    writeln ('o salario liquido e de ', salLiq:4:2 , ' .');
    writeln ('e sua classificacao e BEM REMUNERADO.');
    end

    else if (salLiq <= 600) and (salLiq >= 350) then
            begin
            writeln ('o valor de cada hora trabalhada e de ', valHora:4:2 , ' .');
            writeln ('o valor do salario bruto e de ', salBruto:4:2 , ' .');
            writeln ('o valor de imposto pago e de ', imp:4:2 , ' .');
            writeln ('a gratificacao recebida e de ', grat , ' .');
            writeln ('o valor do auxilio alimentacao e de ', auxilio:4:2 , ' .');
            writeln ('o salario liquido e de ', salLiq:4:2 , ' .');
            writeln ('e sua classificacao e NORMAL.');
            end

            else if (salLiq < 350) then
                    begin
                    writeln ('o valor de cada hora trabalhada e de ', valHora:4:2 , ' .');
                    writeln ('o valor do salario bruto e de ', salBruto:4:2 , ' .');
                    writeln ('o valor de imposto pago e de ', imp:4:2 , ' .');
                    writeln ('a gratificacao recebida e de ', grat , ' .');
                    writeln ('o valor do auxilio alimentacao e de ', auxilio:4:2 , ' .');
                    writeln ('o salario liquido e de ', salLiq:4:2 , ' .');
                    writeln ('e sua classificacao e MAL REMUNERADO.');
                    end;

 writeln (' ');
 write ('para encerrar o programa precione qualquer tecla.');
 readkey;

end.