# Generated by Django 5.0.1 on 2024-03-02 22:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fipe_app', '0025_remove_lead_city_remove_lead_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='city',
            field=models.CharField(choices=[('Abaiara', 'Abaiara'), ('Acarape', 'Acarape'), ('Acaraú', 'Acaraú'), ('Acopiara', 'Acopiara'), ('Aiuaba', 'Aiuaba'), ('Alcântaras', 'Alcântaras'), ('Altaneira', 'Altaneira'), ('Alto Santo', 'Alto Santo'), ('Amontada', 'Amontada'), ('Antonina do Norte', 'Antonina do Norte'), ('Apuiarés', 'Apuiarés'), ('Aquiraz', 'Aquiraz'), ('Aracati', 'Aracati'), ('Aracoiaba', 'Aracoiaba'), ('Ararendá', 'Ararendá'), ('Araripe', 'Araripe'), ('Aratuba', 'Aratuba'), ('Arneiroz', 'Arneiroz'), ('Assaré', 'Assaré'), ('Aurora', 'Aurora'), ('Baixio', 'Baixio'), ('Banabuiú', 'Banabuiú'), ('Barbalha', 'Barbalha'), ('Barreira', 'Barreira'), ('Barro', 'Barro'), ('Barroquinha', 'Barroquinha'), ('Baturité', 'Baturité'), ('Beberibe', 'Beberibe'), ('Bela Cruz', 'Bela Cruz'), ('Boa Viagem', 'Boa Viagem'), ('Brejo Santo', 'Brejo Santo'), ('Camocim', 'Camocim'), ('Campos Sales', 'Campos Sales'), ('Canindé', 'Canindé'), ('Capistrano', 'Capistrano'), ('Caridade', 'Caridade'), ('Cariré', 'Cariré'), ('Caririaçu', 'Caririaçu'), ('Cariús', 'Cariús'), ('Carnaubal', 'Carnaubal'), ('Cascavel', 'Cascavel'), ('Catarina', 'Catarina'), ('Catunda', 'Catunda'), ('Caucaia', 'Caucaia'), ('Ceará', 'Ceará'), ('Cedro', 'Cedro'), ('Chaval', 'Chaval'), ('Choró', 'Choró'), ('Chorozinho', 'Chorozinho'), ('Coreaú', 'Coreaú'), ('Crateús', 'Crateús'), ('Crato', 'Crato'), ('Croatá', 'Croatá'), ('Cruz', 'Cruz'), ('Deputado Irapuan Pinheiro', 'Deputado Irapuan Pinheiro'), ('Ereré', 'Ereré'), ('Eusébio', 'Eusébio'), ('Farias Brito', 'Farias Brito'), ('Forquilha', 'Forquilha'), ('Fortaleza', 'Fortaleza'), ('Fortim', 'Fortim'), ('Frecheirinha', 'Frecheirinha'), ('General Sampaio', 'General Sampaio'), ('Graça', 'Graça'), ('Granja', 'Granja'), ('Granjeiro', 'Granjeiro'), ('Groaíras', 'Groaíras'), ('Guaiúba', 'Guaiúba'), ('Guaraciaba do Norte', 'Guaraciaba do Norte'), ('Guaramiranga', 'Guaramiranga'), ('Hidrolândia', 'Hidrolândia'), ('Horizonte', 'Horizonte'), ('Ibaretama', 'Ibaretama'), ('Ibiapina', 'Ibiapina'), ('Ibicuitinga', 'Ibicuitinga'), ('Icapuí', 'Icapuí'), ('Icó', 'Icó'), ('Iguatu', 'Iguatu'), ('Independência', 'Independência'), ('Ipaporanga', 'Ipaporanga'), ('Ipaumirim', 'Ipaumirim'), ('Ipu', 'Ipu'), ('Ipueiras', 'Ipueiras'), ('Iracema', 'Iracema'), ('Irauçuba', 'Irauçuba'), ('Itaiçaba', 'Itaiçaba'), ('Itaitinga', 'Itaitinga'), ('Itapajé', 'Itapajé'), ('Itapipoca', 'Itapipoca'), ('Itapiúna', 'Itapiúna'), ('Itarema', 'Itarema'), ('Itatira', 'Itatira'), ('Jaguaretama', 'Jaguaretama'), ('Jaguaribara', 'Jaguaribara'), ('Jaguaribe', 'Jaguaribe'), ('Jaguaruana', 'Jaguaruana'), ('Jardim', 'Jardim'), ('Jati', 'Jati'), ('Jijoca de Jericoacoara', 'Jijoca de Jericoacoara'), ('Juazeiro do Norte', 'Juazeiro do Norte'), ('Jucás', 'Jucás'), ('Lavras da Mangabeira', 'Lavras da Mangabeira'), ('Limoeiro do Norte', 'Limoeiro do Norte'), ('Madalena', 'Madalena'), ('Maracanaú', 'Maracanaú'), ('Maranguape', 'Maranguape'), ('Marco', 'Marco'), ('Martinópole', 'Martinópole'), ('Massapê', 'Massapê'), ('Mauriti', 'Mauriti'), ('Meruoca', 'Meruoca'), ('Milagres', 'Milagres'), ('Milhã', 'Milhã'), ('Miraíma', 'Miraíma'), ('Missão Velha', 'Missão Velha'), ('Mombaça', 'Mombaça'), ('Monsenhor Tabosa', 'Monsenhor Tabosa'), ('Morada Nova', 'Morada Nova'), ('Moraújo', 'Moraújo'), ('Morrinhos', 'Morrinhos'), ('Mucambo', 'Mucambo'), ('Mulungu', 'Mulungu'), ('Nova Olinda', 'Nova Olinda'), ('Nova Russas', 'Nova Russas'), ('Novo Oriente', 'Novo Oriente'), ('Ocara', 'Ocara'), ('Orós', 'Orós'), ('Pacajus', 'Pacajus'), ('Pacatuba', 'Pacatuba'), ('Pacoti', 'Pacoti'), ('Pacujá', 'Pacujá'), ('Palhano', 'Palhano'), ('Palmácia', 'Palmácia'), ('Paracuru', 'Paracuru'), ('Paraipaba', 'Paraipaba'), ('Parambu', 'Parambu'), ('Paramoti', 'Paramoti'), ('Pedra Branca', 'Pedra Branca'), ('Penaforte', 'Penaforte'), ('Pentecoste', 'Pentecoste'), ('Pereiro', 'Pereiro'), ('Pindoretama', 'Pindoretama'), ('Piquet Caneiro', 'Piquet Caneiro'), ('Pires Ferreira', 'Pires Ferreira'), ('Poranga', 'Poranga'), ('Porteiras', 'Porteiras'), ('Potengi', 'Potengi'), ('Potiretama', 'Potiretama'), ('Quiterianópolis', 'Quiterianópolis'), ('Quixadá', 'Quixadá'), ('Quixelô', 'Quixelô'), ('Quixeramobim', 'Quixeramobim'), ('Quixeré', 'Quixeré'), ('Redenção', 'Redenção'), ('Reriutaba', 'Reriutaba'), ('Russas', 'Russas'), ('Saboeiro', 'Saboeiro'), ('Salitre', 'Salitre'), ('Santa Quitéria', 'Santa Quitéria'), ('Santana do Acaraú', 'Santana do Acaraú'), ('Santana do Cariri', 'Santana do Cariri'), ('São Benedito', 'São Benedito'), ('São Gonçalo do Amarante', 'São Gonçalo do Amarante'), ('São João do Jaguaribe', 'São João do Jaguaribe'), ('São Luís do Curu', 'São Luís do Curu'), ('Senador Pompeu', 'Senador Pompeu'), ('Senador Sá', 'Senador Sá'), ('Sobral', 'Sobral'), ('Solonópole', 'Solonópole'), ('Tabuleiro do Norte', 'Tabuleiro do Norte'), ('Tamboril', 'Tamboril'), ('Tarrafas', 'Tarrafas'), ('Tauá', 'Tauá'), ('Tejuçuoca', 'Tejuçuoca'), ('Tianguá', 'Tianguá'), ('Trairi', 'Trairi'), ('Tururu', 'Tururu'), ('Ubajara', 'Ubajara'), ('Umari', 'Umari'), ('Umirim', 'Umirim'), ('Uruburetama', 'Uruburetama'), ('Uruoca', 'Uruoca'), ('Varjota', 'Varjota'), ('Várzea Alegre', 'Várzea Alegre'), ('Viçosa do Ceará', 'Viçosa do Ceará')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='vehicle_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='fipe_app.fipevehicletype'),
            preserve_default=False,
        ),
    ]