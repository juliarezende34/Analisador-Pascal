program float;

var 
    codE, codC: integer;
    peso, novoPeso: real;

begin
    writeln('caro usuario este programa programa lhe mostrara de acordo com os dados que voce inserir, o peso da carga do caminhao.');
    writeln('o preco da carga do caminhao, o valor do imposto do estado, e o valor do produto acrescido do imposto.');
    writeln(' ');
    write('para inciar tecle enter.');

    writeln('primeiramente digite o codigo do estado de origem, de 1 a 5.');
    readln(codE);

    writeln('agora digite o codigo da carga, de 10 a 40.');
    readln(codC);

    writeln('agora digite o peso da carga em toneladas.');
    readln(peso);

    novoPeso := peso * 1000;

    if (codE = 1) then
    begin
        if ((codC >= 10) and (codC <= 20)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 100):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 100) * 0.35):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 100) * 1.35):4:2, ' .');
        end
        else if ((codC >= 21) and (codC <= 30)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 250):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 250) * 0.35):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 250) * 1.35):4:2, ' .');
        end
        else if ((codC >= 31) and (codC <= 40)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 340):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 340) * 0.35):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 340) * 1.35):4:2, ' .');
        end;
    end
    else if (codE = 2) then
    begin
        if ((codC >= 10) and (codC <= 20)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 100):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 100) * 0.25):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 100) * 1.25):4:2, ' .');
        end
        else if ((codC >= 21) and (codC <= 30)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 250):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 250) * 0.25):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 250) * 1.25):4:2, ' .');
        end
        else if ((codC >= 31) and (codC <= 40)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 340):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 340) * 0.25):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 340) * 1.25):4:2, ' .');
        end;
    end
    else if (codE = 3) then
    begin
        if ((codC >= 10) and (codC <= 20)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 100):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 100) * 0.15):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 100) * 1.15):4:2, ' .');
        end
        else if ((codC >= 21) and (codC <= 30)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 250):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 250) * 0.15):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 250) * 1.15):4:2, ' .');
        end
        else if ((codC >= 31) and (codC <= 40)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 340):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 340) * 0.15):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 340) * 1.15):4:2, ' .');
        end;
    end
    else if (codE = 4) then
    begin
        if ((codC >= 10) and (codC <= 20)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 100):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 100) * 0.05):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 100) * 1.05):4:2, ' .');
        end
        else if ((codC >= 21) and (codC <= 30)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 250):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 250) * 0.05):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 250) * 1.05):4:2, ' .');
        end
        else if ((codC >= 31) and (codC <= 40)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 340):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 340) * 0.05):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 340) * 1.05):4:2, ' .');
        end;
    end
    else if (codE = 5) then
    begin
        if ((codC >= 10) and (codC <= 20)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 100):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 100) * 0.0):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 100) * 1.00):4:2, ' .');
        end
        else if ((codC >= 21) and (codC <= 30)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 250):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 250) * 0.00):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 250) * 1.00):4:2, ' .');
        end
        else if ((codC >= 31) and (codC <= 40)) then
        begin
            writeln('o peso da carga em quilos e ', novoPeso:4:2, ' .');
            writeln('o preco da carga e ', (novoPeso * 340):4:2, ' .');
            writeln('o preco do imposto e ', ((novoPeso * 340) * 0.00):4:2, ' .');
            writeln('o valor da carga com imposto e ', ((novoPeso * 340) * 1.00):4:2, ' .');
        end;
    end;

    writeln(' ');
    write('para encerrar o programa precione qualquer tecla.');
    readln;
end.