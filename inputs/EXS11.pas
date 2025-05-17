program exs11;



var horaI,horaF,minI,minF,horaD,minD: integer;

//se declara as variaveis que serao utilizadas.

begin;

 //se apresenta o programa para o usuario

 clrscr;
 writeln ('caro usuario este programa lhe mostrara a duracao de um jogo baseado na hora de inicio e fim.');
 write ('para comecar tecle enter');
 readkey;

 //ento se comea a adquirir os valores das variaveis.

 clrscr;
 writeln ('primeiramente digite a hora que o jogo comecou, numeros de 00-23.');
 readln (horaI);

 clrscr;
 writeln ('agora digite os minutos do primeiro horario.');
 readln (minI);

 clrscr;
 writeln ('agora digite a hora que o jogo terminou, numeros de 00-23.');
 readln (horaF);

 clrscr;
 writeln ('agora digite os minutos do segundo horario.');
 readln (minF);

 //agora se abre a cadeia de ifs. Para casos mais simples como a hora final e minuto final maior que os iniciais.
 //simplesmente  nescessario diminuir da hora final a hora inicial e o mesmo com os minutos.

 clrscr;

 if (horaF > horaI) and (minF > minI) then
    begin
    writeln ('o jogo durou ',horaF - horaI, ' horas e ', minF - minI, 'minutos .');
    end

    //agora quando os minutos finais tem um valor menor que os minutos iniciais j  nescessario diminuir uma hora do total de horas
    //e subtrair os minutos finais com 60 que  o valor da hora diminuida com o valor dos minutos iniciais.

    else
        if (horaF > horaI) and (minF < minI) then
           begin
           writeln ('o jogo durou ',(horaF - horaI)-1 ,' horas ', (minF+60)-minI, ' minutos .'); readkey;
           end

           //agora para o caso da hora inicial ser maior que a final o tratamento  diferente.
           //porem para o caso dos minutos iniciais forem maior que os finais o tratamento  o mesmo
           //no caso da hora inicial ser maior que a final, se soma a hora final com 24 e depois se substrai pela hora inical


           else begin

               if minI > minF then
                  begin
                  minF  := minF+60;
                  horaF := horaF-1;
                  end;

               if horaI > horaF then
               begin
               horaF := horaF + 24;
               minD  := minF - minI;
               horaD := horaF - horaI;
               end;

               //entao a unica coisa restante  mostrar para o usuario o valor de durao do jogo.

               writeln ('o jogo durou ',horaD,' horas ',minD, ' minutos.');
                end;

 writeln (' ');
 write ('para encerrar o programa precione qualquer tecla');    readkey;

end.
