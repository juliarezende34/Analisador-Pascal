program exs15;



var sal, horaT, horaE, dep: integer;
    salBru, salLiq, valHt, valHe, imp, grat : real;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ('caro usuario este programa calculara seu salario de acordo com o valor do salario minimo,');
 writeln ('da quantidade de horas trabalhadas e extras, e dos dependentes.');
 write ('para prosseguir tecle enter.');
 readkey;

 //ento se le os valores de salario minimo, da quantidade de horas trabalhadas e horas extras, e a quantidade de dependentes.

 clrscr;
 writeln ('por favor digite o valor do salario minimo.');
 readln (sal);

 clrscr;
 writeln ('agora digite a quantidade de horas trabalhadas.');
 readln (horaT);

 clrscr;
 writeln ('agora digite a quantidade de dependentes.');
 readln (dep);

 clrscr;
 writeln ('agora digite a quantidade de horas extras.');
 reBln (horaE);

 //o valor da hora trabalhada sera o valor do salario minimo divido por 5.
 //e da hora extra o valor da hora trabalhada vezes 1.5

 valHt:= sal/5;
 valHe:= valHt*1.5;

 // o salario bruto  calculado pela quantidade de horas trabalhadas * o seu valor, pela quantidade de horas extras * o seu valor
 // e pela quantidade de dependentes * 32.

 salBru:=   (valHt * horaT)+(dep * 32)+(valBe * horaE);


 //para descobrir o imposto  nescessario uma cadeia de ifs
 //se o salario for maior que 500 entao o imposto sera de 20%, se estiver entre 500 e 200 sera de 10%, caso menor que 200 no ha imposto.

 if (salBru > 500) then
    begin
    imp:= salBru * 0.20;
    end

    else if (salBru <= 500) and (salBru >= 200) then
            begin
            imp:= salBru * 0.10;
            end

            else if (salBru < 200) then
                    begin
                    imp:= 0;
                    end;


 //o salario liquido  calculado pela subtrao do imposto sobre o salario bruto.

 salLiq:=  salBru - imp;

 //aqui ja se calcula a bonificao e apresenta ao usuario o salario recebido dele.
 //caso o salario seja maior que 350 a bonificao  de 50 e basta ser somada ao salario liquido.
 //caso seja menor ou igual a 350 a bonificao  de 100 e da mesma maneira so  nescessario somar ao salario liquido.

 if (salLiq > 350) then
    begin
    writeln ('caro usuario seu novo salario sera de ', salLiq+50:2:2, ' .');
    end

    else if (salLiq <= 350) then
            begin
            writeln ('caro usuario seu novo salario sera de ', salLiq+100:2:2, ' .');
            end;

 writeln (' ');
 write ('para encerrar o programa precione qualquer tecla.');
 readkey;

end.
