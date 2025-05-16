program exs25;



var angulo, voltas, novoAng, : integer;

begin;


 //depois de se declarar as variaveis se apresenta o resumo do programa ao usuario.

 clrscr;
 writeln ('caro usuario este programa recebera um angulo e lhe dira em que quadrante ele esta,');
 writeln ('quantas voltas ele deu, e em qual sentido foi a volta.');
 write ('para iniciar tecle enter.');
 readkey;

 clrscr;
 writeln ('primeiramente digite o angulo.');
 readln (angulo);

 //ento se le o angulo que o usuario digita.

 clrscr;

 {Para se descobrir quanto ser o angulo, se usa mod do angulo por 360 e
 dessa maneira se acha o resto da diviso do angulo por 360.}
 {E para se descobrir o numero de voltas se faz a operao de div do angulo por
  360.}

 novoAng:= angulo mod 360;
 voltas:=   angulo div 360;

 {Se cria uma condio para quando o angulo for menor que 0 para se calcular
  em qual quadrante o angulo esta.}

 if (novoAng < 0) then
    begin
    novoAng:= novoAng + 360;
    end;

 {Se cria uma condio para que se o usuario digitar uma opo que o angulo em questo
  esteja em cima dos eixos, se apresenta uma mensagem falando e se encerra o programa.}

 if (novoAng=0) or (novoAng=90) or (novoAng=180) or (novoAng=270) or (novoAng=360) then
    begin
    writeln ('Este angulo esta em cima de algum dos eixos.');
    write ('para encerrar o programa precione qualquer tecla.');
          readkey;       exit;
    end;

 {Para se descobrir em qual quadrante o angulo est basta pegar o resultado do
  mod do angulo e o colocar em uma cadeia de ifs, onde j se apresenta ao usuario
  em qual quadrante est o angulo.}

 if (novoAng > 0) and (novoAng < 90) then
    begin
    writeln ('Este angulo esta no primeiro quadrante.');
    end

    else if (novoAng > 90) and (novoAng < 180) then
            begin
            writeln ('Este angulo esta no segundo quadrante.');
            end

            else if (novoAng > 180) and (novoAng < 270) then
                    begin
                    writeln ('Este angulo esta no terceiro quadrante.');
                    end

                    else if (novoAng > 270) and (novoAng < 360) then
                            begin
                            writeln ('Este angulo esta no quarto quadrante.');
                            end;


 {para descobrir o sentido do angulo basta criar uma condio para que se o angulo inicial
 for menor que 0 entao sera sentido anti horario caso contrario sera sentido horario.}

 if (angulo < 0) then
    begin
    writeln (voltas,' so sentido anti horario.');
    end

    else begin
         writeln (voltas, ' no sentido horario.');
         end;


 writeln (' ');
 writeln ('Para encerrar o programa precione qualquer tecla.');   readkey;

end.
