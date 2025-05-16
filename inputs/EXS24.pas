program exs24;



var preco, valAdd, imp, precoCusto, desconto, novoPreco : real;
    tipo, refri: char;
    classificacao: string;

begin;

 {depois de se declarar as variaveis, se da o resumo do programa ao usuario.}

 clrscr;
 writeln ('caro usuario este programa recebera o valor de preco, e dois codigos de produto e lhe mostrara o valor adicional, ');
 writeln ('o valor do imposto, o preco de custo, o desconto, o novo preco e a classificacao do produto.');
 write ('para prosseguir tecle enter.');
 readkey;

 clrscr;
 writeln ('primeiro digite o preco do produto.');
 readln (preco);

 clrscr;
 writeln ('agora digite o codigo do produto A para alimentacao ,L para limpeza ,V para vestuario .');
 writeln ('Lembre-se de usar somente letras maiusculas.');
 readln (tipo);

 clrscr;
 writeln ('agora digite o codigo que representa se o produto nessecita de refrigeracao ou nao. S se precisar e N se nao precisar.');
 writeln ('Lembre-se de usar somente letras maiusculas.');
 readln (refri);

 {depois se l os valores das variaveis que sero utilisados nas estruturas case e if.
  Na primeira estrutura case se coloca um outro case dentro dele, e dentro de cada case faz-se uma pequena cadeia if
   para definir o valor adicional.}

 case refri of
    'N': begin
           case tipo of
              'A': begin if (preco < 15) then
                            begin
                            valAdd:= 2;
                            end

                            else if (preco >= 15) then
                                    begin
                                    valAdd:= 5;
                                    end;
                   end;


              'L': begin if (preco < 10) then
                            begin
                            valAdd:= 1.50;
                            end

                            else if (preco >= 10) then
                                    begin
                                    valAdd:= 2.50;
                                    end;
                   end;

              'V': begin if (preco < 30) then
                            begin
                            valAdd:= 3;
                            end

                            else if (preco >= 30) then
                                    begin
                                    valAdd:= 2.50;
                                    end;
                   end;

           end;
         end;

    'S': begin  if (tipo = 'A') then
                   begin
                   valAdd:=8;
                   end

                   else if (tipo = 'L') or (tipo = 'V') then
                           begin
                           valAdd:=0;
                           end;
         end;
 end;


 if (preco < 25) then
    begin
    imp:= preco*0.05;
    end

    else if (preco >= 25) then
            begin
            imp:= preco*0.08;
            end;

 //ento se calcula o preco de custo do produto.

 precoCusto:= preco + imp;

 {Para definir o valor do desconto se depende de duas variaveis e impondo a condio sobre elas se calcula o valor
   do desconto.}

 if (tipo = 'A') and (refri = 'S')  then
    begin
    desconto:=0
    end

    else
        begin
        desconto:= precoCusto*0.03;
        end;

 //ento se calcula o novo preo para que se possa definir a classificao do produto.

 novoPreco:= precoCusto - desconto + valAdd;

 {a classificao do produto  definida a partir do valor do novo preo.
  A cada condio imposta vai ser uma classificao.}

 if (novoPreco <= 50) then
    begin
    classificacao:= 'barato';
    end

    else if (novoPreco > 50) and (novoPreco < 100) then
            begin
            classificacao:= 'normal';
            end

            else if (novoPreco >= 100) then
                    begin
                    classificacao:= 'caro';
                    end;


 //ento a unica coisa restante  limpar a tela para mostrar ao usuario os resultados.

 clrscr;

 writeln ('o valor adicional e de ', valAdd:4:2 , ' .');
 writeln ('o valor do imposto e de ', imp:4:2 , ' .');
 writeln ('o preco de custo e de ', precoCusto:4:2 , ' .');
 writeln ('o desconto e de ', desconto:4:2 , ' .');
 writeln ('o novo preco e de ', novoPreco:4:2 , ' .');
 writeln ('a classificacao e ', classificacao , ' .');

 writeln (' ');
 write ('para encerrar o programa precione qualquer tecla');  readkey;

end.
