program exs16;

uses crt;

var n1: integer;
    n2: real;

begin;

 //depois de se declarar as variaveis, se apresenta um resumo do programa ao usuario.

 clrscr;
 writeln ('caro usuario este programa lhe mostrara o novo preco do produto de acordo com a venda mensal e seu preo.');
 write ('para prosseguir tecle enter.');
 readkey;

 //se le os valores do preo do produto e da venda mensal do mesmo.

 clrscr;
 writeln ('por favor digite o preco do produto.');
 readln (n1);

 clrscr;
 writeln ('agora digite a venda mensal do produto');
 readln (n2);

 clrscr;

 //e depois se comea a cadeia de ifs para determinar o novo preo do produto
 //com as condies impostas j se apresenta ao usuario o novo valor do produto fazendo simples calculos de mutiplicao.

 if (n2 >= 1200) or  (n1 >= 80) then
    begin
    writeln ('o novo preco do produto e ', n1*0.80:4:2, ' .');
    end

    else if (n2 >= 500) or ((n1 >= 30) and (n1<80)) then
            begin
            writeln ('o novo preco do produto e ', n1*0.15:4:2, ' .');
            end

            else if (n2<500) or (n1<30) then
                    begin
                    writeln ('o novo preco do produto e ', n1*0.10:4:2, ' .');
                    end;

 writeln (' ');
 write ('para encerrar o programa precione qualquer tecla.');
 readkey;

end.
