program exs3;

uses crt;

var n1,n2: real;

begin;

 clrscr;
 writeln ('caro usuario este programa mostrara qual dos numeros que voce inseriu e o maior deles');
 write ('para comecar tecle enter');
 readkey;

 clrscr;
 writeln ('por favor digite o primeiro numero e tecle enter ');
 readln (n1);

 clrscr;
 writeln ('agora digite o segundo numero e tecle enter ');
 readln (n2);

 //primeiro se le os dois numeros que o usuario digitou, ento voce faz as 3 condies possiveis, que nesse caso so.
 //o n1 maior que o n2, o contrario desta situao, e ambos os numeros iguais.
 //ento so resta digitar os comandos para cada caso.

 clrscr;
 if n1 > n2
   then   begin
          writeln ('o numero maior e , ', n1:4:2, '.');
          end

         else if (n1 < n2)
                then  begin
                      writeln ('o numero maior e , ', n2:4:2, '.');
                      end

                   else if (n1=n2)
                          then begin
                               writeln ('os dois numeros sao iguais.');
                               end;


        writeln (' ');
        write ('para encerrar o programa aperte qualquer tecla.');
        readkey;

end.
