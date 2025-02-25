# Lurrikarak Kafka bidez
Jarduera hau, IsardVDI bezalako ingurune batean prestatzeko pentsatua izan da. Makina birtualera sarbidea lortu eta pasahitz gabeko ssh gako bidezko sarbidea prestatu ondoren exekutatu beharko da.

Prozesuak lehenengo sare lokala prestatuko du. Kafka brokerra sare lokal bateko IP finko batean egongo da. Gainera sare horretan bertan DCHCP zerbitzari bat ezarriko dugu. Kasu honetan brokerra dagoen makina berean. Sarearen konfigurazio guztia burutzeko Ansible erabiliko dugu.

## Kafka eta Zookeper
Ansible erabilita instalatuko dira IP finkoa duen makinan.

## Lurrikara producerra
Ansible bitartez beharrezkoak diren python pakete guztiak instalatu eta producerra inplementatuko duen scripta kopiatu eta zerbitzu bezala ezarriko da. Guzti hau kafka erabiltzailea erabilita burutuko da ``/opt/kafka`` direktoriopean.

## Lurrikara kontsumerra
Hau inplementatzeko beste **bezero** makina bat prestatuko da, sare berean eta IP-a DHPC bitartez hartuko duelarik.
Honetarako ere Ansible erabiliko da.
## Exekuzioa
``ansible-playbook -i inventory.ini main.yml --ask-become-pass``

