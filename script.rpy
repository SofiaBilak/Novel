define m = Character("Максвел", color="#597bd1")
define n = Character("Неллі", color="#cf5488")
define nn = Character("???")
define bob = Character("Боб", color="#37ff00")

label start:
    scene bg location1
    show maks neutral

    m "Я не розумію де знаходжуся."
    m "Я не розумію чи я взагалі існую..."
    m "...чи мене хтось помічає, цінує, чи любить..."

    m "Я знаю тільки одне: я тут, у цьому безмежному просторі, де немає ні світла, ні звуку, ні тепла, ні холоду..."
    m "Тут немає нічого, окрім мене і моїх думок."

    m "Як я сюди потрапив? Я не пам'ятаю, що було раніше. Я не пам'ятаю, що призвело до цього..."
    m "Чи це був сон, чи реальність..."
    m "Я пам'ятаю тільки як я був щасливим."

    m "І тепер я тут, у цій пітьмі, де я наодинці з власними думками. І мені тут добре..."
    m "Мені добре, бо я не відчуваю болю..."
    m "Не маю жодних потреб..."
    m "Мені добре, бо я ні від кого не залежу..."
    m "Не несу ніякої відповідальності."

    m "Я не сподіваюся ні на що."
    m "Я не сподіваюся на диво..."
    m "...на сигнал..."
    m "...на голос."

    m "Я просто живу...Живу в своєму світі..."
    m "Я живу в своїй пітьмі, в своїй ейфорії."
    m "Я живу у своїй байдужості...Я живу для себе, для своїх думок, спогадів і почуттів."

    nn "???"

    "Максвел почув якийсь невідомий шум здалеку."

    nn "???"

    nn "Прокинься!"

    "Головний герой розплющив очі і побачив перед собою розмитий силует."
    "Йому кортіло спитати котра година, проте, відкривши очі, він побачив не свою маму, а когось іншого."

    m "Де я? Хто ти? Що тут взагалі відбувається?"
    hide maks neutral
    show nelli neutral

    n "Мене звати Неллі. - відповіла занепокоїно дівчина. - Я прокинулась досить давно, в мене ніяк не виходило розбудити тебе."
    hide nelli neutral
    show maks neutral

    m "Як я тут опинився? Це ти в цьому винна?!"
    hide maks neutral
    show nelli neutral

    n "Я розумію, що ти наляканий, але не потрібно кричати. Я також не розумію, як ми сюди потрапили."

    m "..."

    n "Як я можу звертатись до тебе?"
    hide nelli neutral
    show maks neutral

    m "Я Максвел, але можна просто Макс."
    hide maks neutral

    "Максвел і Неллі ретельно досліджують підземелля, обговорюючи місцеві дивовижності."
    show maks neutral
    m "(сам до себе) Дивно, тут відносно світло для підземелля. І ці камені... чому вони світяться?"
    hide maks neutral
    show nelli neutral
    n "(розмірковуючи) Ніколи не бачила такого, мене це лякає."
    hide nelli neutral
    show maks neutral
    m "А от ці кістки та черепи... це виглядає тривожно."
    hide maks neutral
    show nelli neutral
    n "Можливо, це тут давно, і ми не перші, хто опинився в цьому місці... Що нам робити?"
    hide nelli neutral
    show maks neutral
    m "Не знаю, але ці черепи ставлять під сумнів нашу безпеку."
    m "Ми повинні бути обережними та не залишатись тут надто довго."
    hide maks neutral

    label choices:
menu:
    "Запитатися в Неллі, чи вона згідна іти в напрямку світла...":
        jump choices1_a
    "Сказати Неллі, що це місце виглядає небезпечно, та що краще дочекатися допомоги...":
        jump choices1_b
label choices1_a:
    show maks neutral
    m "Неллі, може, нам варто рухатися в напрямку світла? Можливо, це виведе нас до виходу..."
    hide maks neutral
    show nelli neutral
    n "Ходімо. Сподіваюсь, це допоможе нам вибратись звідси..."
    hide nelli neutral
    jump choices1_common

label choices1_b:
    show maks neutral
    m "Неллі, це місце виглядає небезпечно. Можливо, нам краще дочекатися допомоги..."
    m "Щось тут не так, і нам слід бути обережними..."
    hide maks neutral
    show nelli neutral
    n "Ми вже чекаємо допомоги так довго і нічого не змінилося..."
    n "Ми одні в підземеллі, не відомо де, і навіть не відомо, чи хтось узагалі дізнається, що ми тут..."
    n "Ти дійсно думаєш, що нам хтось допоможе?"
    hide nelli neutral
    show maks neutral
    m "Але, можливо, якщо ми продовжимо чекати, то нас знайдуть..."
    hide maks neutral
    show nelli neutral
    n "Макс, але ми самі залишаємося у цьому місці, і навіть не знаємо, як сюди потрапили..."
    n "Я не впевнена, що ми дочекаємося на чудо..."
    n "Можливо, саме зараз ми повинні взяти справу в свої руки і шукати вихід..."

    n "Давай оглянемо це місце!"
    hide nelli neutral
    show maks neutral
    m "Добре. Як ти вже казала, разом ми зможемо подолати це..."

    jump choices1_common

label choices1_common:
    # газета
    "ПІДЗЕМЕЛЛЯ ТАЄМНИЦЬ(випуск від 10 листопада 1998р.)"
    "Таємничі Підземелля: Що Сховано Глибоко Під Землею?\n
    У дебрях підземелля, відомого лише кільком обранцям, розкривається неймовірна таємниця. На перший погляд, це просто система тунелів, але є чимось надзвичайним."
    "Інформація від зниклих:\n
    Багато виживших, які вибрались з підземелля,  давали дивовижні свідчення. Один із них стверджує, що знайшов вихід, але він привів його в інший, ще загадковіший." 
    "Станом на сьогодні відомо що більше 50 осіб рахуються пропавшими безвісти, вижівші стверджують, що ці особи так і не знайшли вихід з цього підземелля."
    "Світло каменів: \n
    Одна з особливостей цього підземелля - світле освітлення. Дрібні камені на стінах випромінюють світло, створюючи ефект неповторної підземної атмосфери. Чим це зумовлено, досі невідомо."
    "Психологічний стан дослідників: \n
    Останній випадок зникнення відзначений галюцинаціями та станами паніки. Деякі називають це ефектом загадкових газів, але науковці розглядають це як реакцію на низький рівень кисню."
    "Наукові теорії: \n
    Науковці намагаються знайти відповіді на таємниці цього підземельного світу. Деякі теорії стверджують, що низький рівень кисню та природні гази можуть впливати на психіку дослідників."
    "Чи є вихід? \n
    Багато дослідників зазначають, що знайшли вихід, але його місцезнаходження залишається суворою таємницею. За останні роки чисельні експедиції не поверталися."
    "Ми продовжуємо слідкувати за подіями в підземеллях та розкривати їхні таємниці."
    
    show maks neutral
    m "(з газетою в руках) Неллі, поглядай на цю статтю. Підземелля Таємниць. Це те саме місце, яке ми зараз досліджуємо. "
    hide maks neutral
    show nelli neutral
    n "(зацікавлено) Що тут написано?"
    hide nelli neutral
    show maks neutral
    m "(читає вголос) Багато відважних розпочинали свою подорож у ці загадкові підземелля, але лише кілька поверталися. Більшість зникли безвісти. Деякі стверджують, що бачили дивовижні створіння, інші впадали в галюцинації..."
    hide maks neutral
    show nelli neutral
    n "(налякано) Чи ми не впадемо в галюцинації? Це все реально?"
    hide nelli neutral
    show maks neutral
    m "Науковці стверджують, що це може бути пов'язане з низьким рівнем кисню та природними газами у підземеллях. Але щось мені підказує, що це не тільки наука."
    m "Ми повинні залишатися насторожі. Нам доведеться бути розумнішими за тих, хто раніше намагався вибратися звідси."
    hide maks neutral
    show nelli neutral
    n "Ми неодмінно знайдемо вихід, Макс. Я вірю в нас."
    hide nelli neutral

    # записка

    "У цих кам'яних стінах спочиває розгадка, Три руни відкриють тобі вихід в світло."
    show maks neutral
    m "(подумки) Руни на кам'яних стінах... це може бути підказка..."
    hide maks neutral

    # ліхтарик
    # якщо обрали ліхтарик:

    show maks neutral
    m "(подумки) А ось це тут точно не буде зайвим."

    # записка

    m "(подумки) Якись дивний набір символів, нічого не можу розібрати"

    # скеля
    # якщо обрали скелю:

    hide maks neutral
    show nelli neutral
    n "Макс, можливо, нам потрібно знайти ці руни та вставити їх у скелю. Я впевнена, це ключ до виходу."
    hide nelli neutral

menu:
    "Погодитись з Неллі і разом з нею шукати руни":
        jump choices2_a
    "Висловити сумніви та запитати, чому вони взагалі повинні вставляти руни, можливо, є інший вихід.":
        jump choices2_b
label choices2_a:
    show maks neutral
    m "Так, ти маєш рацію. Ми повинні їх знайти, можливо це допоможе нам вибратись звідси."
    hide maks neutral
    jump choices2_common

label choices2_b:
    show maks neutral
    m "Неллі, навіть якщо ми вставимо ці руни, нічого не відбудеться. Це не гра"
    hide maks neutral
    show nelli neutral
    n "Я розумію твої сумніви. Але ми не можемо просто чекати тут без дії."
    n "Я вірю, що це може спрацювати. Давай спробуємо, може, ми знайдемо вихід разом"
    hide nelli neutral
    show maks neutral
    m "Добре, Неллі. Хоч це і звучить безглуздо, але варіантів небагато"
    hide maks neutral
    jump choices2_common

label choices2_common:
    # руни
    "Великі кам'яні брили відокремлюються, і скеля розсувається, відкриваючи новий прохід. Максвел та Неллі стоять в повному шоці, бо стали свідками дива"
    show maks neutral
    m "Що за... Я не міг уявити, що це може відбутися. Це не землетрус, це... це щось надприродне."
    hide maks neutral
    show nelli neutral
    n "Макс, ти бачиш це? Скелю тільки що розсунуло, мов намагається відкрити нам шлях. Це неймовірно!"
    hide nelli neutral
    jump new_choices

label new_choices:
    menu:
        "Залишитись разом і продовжити дослідження того, що вже відкрито":
            jump choices3_a
        "Піти вперед":
            jump choices3_b
    label choices3_a:
        show maks neutral
        m "Неллі, можливо, краще залишитись тут і докладніше роздивитись оті руни?"
        m "Що якщо ще є якась важлива інформація, яку ми пропустили?"
        hide maks neutral
        show nelli neutral
        n "Ти впевнений? Мені здається, що нам варто йти вперед. Хто знає, що ще може бути за тим поворотом."
        n "Можливо, це ключ до виходу."
        hide nelli neutral
        jump choices3_common
    label choices3_b:
        show maks neutral
        m "Неллі, я вважаю, що нам потрібно піти вперед. Скеля відкрилась, і хто знає, що нас чекає далі. Можливо, це дорога до виходу."
        hide maks neutral
        show nelli neutral
        n "Ти правий, Макс. Давай підемо разом і дізнаємося, що там."
        hide nelli neutral
        jump choices3_common
    label choices3_common:
        # Коли гравець потрапив на локацію 2
        show nelli neutral
        n "Макс, ти чув? Нічого не видно, мені здається, що тут ми не одні..."
        hide nelli neutral
        show bob light
        nn "Бу!!! Злякались?"
        hide bob light

        show maks neutral
        m "Ти в своєму розумі? Що відбувається?"
        hide maks neutral
        show bob happy
        bob "Та що ти? Мене звати Боб. Ви також застрягли тут як і я?"
        hide bob happy
        show maks neutral
        m "Виходить, що так"
        hide maks neutral
        show bob happy
        bob "А сказати як вас звати, ви не хочете представитись?"
        hide bob happy
        show maks neutral
        m "Ну, Її звати Неллі, мене Максвел"
        hide maks neutral
        show bob happy
        bob "Максвел?? А-ха-ха-ха, так звали улюблену собаку моєї тітки!"
        hide bob happy
        m "..."
        "Неллі, Максвел та Боб попрямували далі"
        show maks neutral
        m "(подумки) Не буду казати Бобу про те, що в нас є ліхтарик"
        hide maks neutral
        show bob happy
        bob "Це таке диво! Я взагалі не розумію, як я сюди потрапив"
        bob "Пошукавши довкола, я натрапив на дивну записку. Там написано, що є зачароване дзеркало, яке не відображає, і потрібно зібрати його..."
        hide bob happy
        show nelli neutral
        n "Ти що-небудь розібрав з цієї головоломки?"
        hide nelli neutral
        show bob happy
        bob "Я вже не першу годину пробую його зібрати, але марно, мені потрібна допомога."
        "Боб передає записку Максвелу і Неллі"
        hide bob happy
        "Серед темряви та відламаних відбитків, Дзекало приховує чарівну таємницю. Збери його частини, і світло розкриється, Дорогу вибереш, коли об'єднаєш його в цілісність."
        # іграшковий літак
        show maks neutral
        m "(подумки)Якись дивний набір символів, нічого не можу розібрати"
        # фотоапарат
        "Відеокамера. На його корпусі присутні сліди масла"
        m "Ця відеокамера виглядає як новенька. Здається, що тут недавно хтось був. Але шкода, що вона заблокована паролем. Навіть не можу переглянути що на ній"
        m "Можливо, у нас є шанс дізнатися більше про те, що тут трапилось, якщо вдасться розгадати цей пароль"
        hide maks neutral

        # Гравець може нажати на дзеркало, починаючи складати по факту пазл до купи
        # Якщо зібрав, Дзеркало відновлюється і показується лист
        # зміст листа:
        "Дорога Маргарет, \n Любов моя, як добре було б тут нам разом. Кожен день, коли ти не зі мною, стає набагато важчим. Моє серце б'ється лише за тобою, і я дуже сумую."
        "Ти завжди була для мене опорою і найкращим другом. Немає дня, коли я не думаю про тебе та той момент, коли знову буду біля тебе. Ти - моє світло, яке освітлює мій шлях, і я не можу дочекатися того дня, коли це світло знову освітить моє життя."
        "Щоби ми були разом, мені доведеться виїхати в невелике відрядження. Я залишу місто 17 липня і повернуся назад в кінці місяця. Обіцяю, що ця розлука зміцнить наше кохання і наш зв'язок. Незважаючи на відстань, ми завжди поруч. Скоро ми знову будемо разом, і я зможу тримати тебе в своїх обіймах."
        "З любов'ю, \n Томас"

        "Максвел, прочитавши цей діалог, почув дивний звук, повернувши дзеркало, він побачив  карточку, на якій написано '17'"

        show maks neutral
        m "Що за...? Неллі, чула цей дивний звук? І подивись, що я тут знайшов. Напис з числом '17'. Як воно пов'язане з усім цим?"
        hide maks neutral
        show nelli neutral
        n "Думаю, це число пов'язане з листом. Томас писав, що він вирушає у відрядження 17 липня. Можливо, це той момент, коли він туди поїхав."
        hide nelli neutral

    
return
