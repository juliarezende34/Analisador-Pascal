program exs14;



var sal,bon,aux,novoSal: real;

begin;

 //depois de se declarar as variaveis se da um resumo do programa para o usuario

 clrscr;
 writeln ('caro usuario este programa lhe mostrara seu novo salario com bonificacao e auxilio escola.');
 write ('para prosseguir tecle enter.');
 readkey;

 // entao se le o salario dele para se fazer os calculos de bonificao e auxilio escola.

 clrscr;
 writeln ('por favor digite o seu salario.');
 readln (sal);

 // o calculo da bonificao  feita em uma cadeia de ifs onde a condio atendida sera somada ao salario inicial
 // juntamente com o auxilio escola.

 if (sal > 1200) then
    begin
    bon:= 0;
    end

    else if (sal <= 1200) and (sal >= 500) then
            begin
            bon:= sal*0.12;
            end

            else if (sal < 500) then
                 begin
                 bon:= sal*0.05;
                 end;


  //como o auxilio escola so tem duas condies se a primeira no for atendida automaticamente sera calculada a segunda

 if (sal > 600) then
    begin
    aux:= 100;
    end

    else
        begin
        aux:= 150;
        end;

 //ento a unica coisa restante  calcular o novo salario e o apresentar ao usuario.

 novoSal:= sal+bon+aux;

 clrscr;
 writeln ('caro usuario seu novo salario e ', novoSal:4:2 , ' .');
 writeln (' ');
 write ('para encerrar o programa precione qualquer tecla.');
 readkey;

end.
