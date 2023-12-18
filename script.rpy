define config.mouse = { }
define config.mouse['default'] = [ ("gui/cursor.png", 0, 0) ]

#Define chars
define m = Character("Максвел", color="#13244f")
define n = Character("Неллі", color="#6f4a19")
define nn = Character("???")
define bob = Character("Боб", color="#23421b")

#Define audio
define audio.background = "audio/backgroundMusic.mp3"
define audio.boo = "audio/boo.mp3"
define audio.scream = "audio/scream.mp3"
define audio.rustle = "audio/unknownRustle.mp3"
define audio.runas1 = "audio/runasFind1.mp3"
define audio.door = "audio/stoneDoor.mp3"
define audio.flashlight = "audio/flashlightOn.mp3"

label start:
    play music background volume 3

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
    
    "Я розплющив очі і побачив перед собою розмитий силует."
    scene bg next:
        blur 15
    show nelli_neutral_hands_behind at center:
        blur 15
    "Мене кортіло спитати котра година, проте, відкривши очі, я побачив не свою маму, а когось іншого."

    #hide nelli_neutral_hands_behind
    m "Де я? Хто ти? Що тут взагалі відбувається?"
    show nelli_neutral_hands_behind

    n "Мене звати Неллі. - відповіла занепокоїно дівчина. - Я прокинулась досить давно, в мене ніяк не виходило розбудити тебе."

    m "Як я тут опинився? Це ти в цьому винна?!"
    hide nelli_neutral_hands_behind

    show nelli second
    n "Я розумію, що ти наляканий, але не потрібно кричати. Я також не розумію, як ми сюди потрапили."
    #hide nelli second

    m "..."

    #show nelli second
    n "Як я можу звертатись до тебе?"
    #hide nelli second

    m "Я Максвел, але можна просто Макс."
    hide nelli second

    "Максвел і Неллі ретельно досліджують підземелля, обговорюючи місцеві дивовижності."
    scene bg location1 with dissolve
    show maks neutral
    m "(сам до себе) Дивно, тут відносно світло для підземелля. І ці камені... чому вони світяться?"
    hide maks neutral

    n "(розмірковуючи) Ніколи не бачила такого, мене це лякає."

    m "А от ці кістки та черепи... це виглядає тривожно."

    n "Можливо, це тут давно, і ми не перші, хто опинився в цьому місці... Що нам робити?"

    m "Не знаю, але ці черепи ставлять під сумнів нашу безпеку."
    m "Ми повинні бути обережними та не залишатись тут надто довго."

    scene bg next with fade

    label choices:
menu:
    "Запитатися в Неллі, чи вона згідна іти в напрямку світла...":
        jump choices1_a
    "Сказати Неллі, що це місце виглядає небезпечно, та що краще дочекатися допомоги...":
        jump choices1_b
label choices1_a:
    m "Неллі, може, нам варто рухатися в напрямку світла? Можливо, це виведе нас до виходу..."

    show nelli second
    n "Ходімо. Сподіваюсь, це допоможе нам вибратись звідси..."
    hide nelli second
    jump choices1_common

label choices1_b:

    m "Неллі, це місце виглядає небезпечно. Можливо, нам краще дочекатися допомоги..."
    m "Щось тут не так, і нам слід бути обережними..."

    show nelli_thinking_arms_on_belt
    n "Ми вже чекаємо допомоги так довго і нічого не змінилося..."
    n "Ми одні в підземеллі, не відомо де, і навіть не відомо, чи хтось узагалі дізнається, що ми тут..."
    n "Ти дійсно думаєш, що нам хтось допоможе?"
    hide nelli_thinking_arms_on_belt

    m "Але, можливо, якщо ми продовжимо чекати, то нас знайдуть..."

    show nelli_angry_arms_on_belt
    n "Макс, але ми самі залишаємося у цьому місці, і навіть не знаємо, як сюди потрапили..."
    n "Я не впевнена, що ми дочекаємося на чудо..."
    n "Можливо, саме зараз ми повинні взяти справу в свої руки і шукати вихід..."
    hide nelli_angry_arms_on_belt

    show nelli neutral
    n "Давай оглянемо це місце!"
    hide nelli neutral

    m "Добре. Як ти вже казала, разом ми зможемо подолати це..."

    jump choices1_common

label choices1_common:
    # Використовуємо imagemap
    call screen firstScreen
    return

label continue_game:
    #scene bg next
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
    

    m "(з газетою в руках) Неллі, поглядай на цю статтю. Підземелля Таємниць. Це те саме місце, яке ми зараз досліджуємо. "

    show nelli_neutral_hands_behind
    n "(зацікавлено) Що тут написано?"
    hide nelli_neutral_hands_behind

    m "(читає вголос) Багато відважних розпочинали свою подорож у ці загадкові підземелля, але лише кілька поверталися. Більшість зникли безвісти. Деякі стверджують, що бачили дивовижні створіння, інші впадали в галюцинації..."

    show nelli_thinking_hands_straight
    n "(налякано) Чи ми не впадемо в галюцинації? Це все реально?"
    hide nelli_thinking_hands_straight

    m "Науковці стверджують, що це може бути пов'язане з низьким рівнем кисню та природними газами у підземеллях. Але щось мені підказує, що це не тільки наука."
    m "Ми повинні залишатися насторожі. Нам доведеться бути розумнішими за тих, хто раніше намагався вибратися звідси."
    show nelli_angry_arms_on_belt
    n "Ми неодмінно знайдемо вихід, Макс. Я вірю в нас."

    hide nelli_angry_arms_on_belt
    jump find_note

label find_note:
    # записка (imagemap)
    call screen secondScreen
    return

label continue_play:
    hide nelli_angry_arms_on_belt
    "У цих кам'яних стінах спочиває розгадка, Три руни відкриють тобі вихід в світло."
    m "(подумки) Руни на кам'яних стінах... це може бути підказка..."
    jump find_flashlight

# ліхтарик (imagemap)
label find_flashlight:
    call screen flashlightFound
    return

label flashlight_found:
    play sound flashlight volume 3.0

    m "(подумки) А ось це тут точно не буде зайвим."

    # скеля (imagemap)
    show nelli neutral
    n "Макс, можливо, нам потрібно знайти ці руни та вставити їх у скелю. Я впевнена, це ключ до виходу."
    hide nelli neutral

menu:
    "Погодитись з Неллі і разом з нею шукати руни":
        jump choices2_a
    "Висловити сумніви та запитати, чому вони взагалі повинні вставляти руни, можливо, є інший вихід.":
        jump choices2_b

label choices2_a:

    m "Так, ти маєш рацію. Ми повинні їх знайти, можливо це допоможе нам вибратись звідси."

    jump choices2_common

label choices2_b:

    m "Неллі, навіть якщо ми вставимо ці руни, нічого не відбудеться. Це не гра"

    show nelli_neutral_hands_behind
    n "Я розумію твої сумніви. Але ми не можемо просто чекати тут без дії."
    n "Я вірю, що це може спрацювати. Давай спробуємо, може, ми знайдемо вихід разом"
    hide nelli_neutral_hands_behind

    m "Добре, Неллі. Хоч це і звучить безглуздо, але варіантів небагато"

    jump choices2_common

label choices2_common:
    # руни
    scene bg next1
    call screen thirdScreen
    return

label first_completed:
    play sound runas1 volume 2.0
    scene bg one with dissolve
    #stop sound
    call screen firstCompleted
    return

label second_completed:
    play sound runas1 volume 2.0
    scene bg two with dissolve
    #stop sound
    call screen secondCompleted
    return

label third_completed:
    play sound runas1 volume 2.0
    scene bg three with dissolve
    #stop sound
    call screen thirdCompleted
    return

label fourth_screen:
    play sound door volume 2.0
    scene bg unlocked with fade
    #stop sound
    jump play_next

label play_next:
    "Великі кам'яні брили відокремлюються, і скеля розсувається, відкриваючи новий прохід. Максвел та Неллі стоять в повному шоці, бо стали свідками дива"

    m "Що за... Я не міг уявити, що це може відбутися. Це не землетрус, це... це щось надприродне."

    show nelli neutral
    n "Макс, ти бачиш це? Скелю тільки що розсунуло, мов намагається відкрити нам шлях. Це неймовірно!"
    hide nelli neutral
    jump new_choices

#вибір шляху після розсування скелі
label new_choices:
    menu:
        "Залишитись разом і продовжити дослідження того, що вже відкрито":
            jump choices3_a
        "Піти вперед":
            jump choices3_b

    label choices3_a:
    
        m "Неллі, можливо, краще залишитись тут і докладніше роздивитись оті руни?"
        m "Що якщо ще є якась важлива інформація, яку ми пропустили?"
    
        show nelli_thinking_hands_behind
        n "Ти впевнений? Мені здається, що нам варто йти вперед. Хто знає, що ще може бути за тим поворотом."
        n "Можливо, це ключ до виходу."
        hide nelli_thinking_hands_behind
        jump choices3_common

    label choices3_b:
    
        m "Неллі, я вважаю, що нам потрібно піти вперед. Скеля відкрилась, і хто знає, що нас чекає далі. Можливо, це дорога до виходу."
    
        show nelli_neutral_arms_on_belt
        n "Ти правий, Макс. Давай підемо разом і дізнаємося, що там."
        hide nelli_neutral_arms_on_belt
        jump choices3_common

    label choices3_common:
        # Коли гравець потрапив на локацію 2
        play sound rustle
        scene bg dark
        show nelli_neutral_arms_on_belt
        #stop sound
        n "Макс, ти чув? Нічого не видно, мені здається, що тут ми не одні, будь тихі..."
        stop sound
        hide nelli_neutral_arms_on_belt
        show bob light
        play sound boo
        #stop sound
        nn "Бу!!! Злякались?"
        stop sound
        #hide bob light
        m "Ти в своєму розумі? Що відбувається?"
        #show bob light
        bob "Та що ти? Мене звати Боб. Ви також застрягли тут як і я?"
        m "Виходить, що так"
        hide bob light
        show bob_hand3
        bob "А сказати як вас звати, ви не хочете представитись?"
        #hide bob_hand3
        m "Ну, її звати Неллі, мене Максвел"
        #show bob light
        hide bob_hand3
        show bob light
        bob "Максвел?? А-ха-ха-ха, так звали улюблену собаку моєї тітки!"
        hide bob light
        m "..."

        scene bg location2
        "Неллі, Максвел та Боб попрямували далі"
        #show maks neutral
        m "(подумки) Не буду казати Бобу про те, що в нас є ліхтарик"
        #hide maks neutral
        show bob light
        bob "Це таке диво! Я взагалі не розумію, як я сюди потрапив"
        bob "Пошукавши довкола, я натрапив на дивну записку. Там написано, що є зачароване дзеркало, яке не відображає особу, і те, що його потрібно зібрати..."
        hide bob light
        show nelli_neutral_arms_on_belt
        n "Ти що-небудь розібрав з цієї головоломки?"
        hide nelli_neutral_arms_on_belt
        show bob light
        bob "Я вже не першу годину пробую його зібрати, але марно, мені потрібна допомога."
        "Боб передає записку Максвелу і Неллі"
        hide bob light
        "Серед темряви та відламаних відбитків, Дзекало приховує чарівну таємницю. Збери його частини, і світло розкриється, Дорогу вибереш, коли об'єднаєш його в цілісність."

        # іграшковий літак
        # записка
        call screen findNote2
        return

#записка з незрозумілими символами
label continue_search:
    m "(подумки)Якись дивний набір символів, нічого не можу розібрати"
    call screen findCamera
    return

label find_camera:
    # фотоапарат
    "Відеокамера. На його корпусі присутні сліди масла"
    m "Ця відеокамера виглядає як новенька. Здається, що тут недавно хтось був. Але шкода, що вона заблокована паролем. Навіть не можу переглянути що на ній"
    m "Можливо, у нас є шанс дізнатися більше про те, що тут трапилось, якщо вдасться розгадати цей пароль"
    call screen firsParticle
    return
    
label keep_searching:
    scene bg location21 with dissolve
    call screen secondParticle
    return

label keep_looking:
    scene bg location22 with dissolve
    call screen lastParticle
    return

label keep_going:
    scene bg location3 with dissolve
    "Дорога Маргарет, \n Любов моя, як добре було б тут нам разом. Кожен день, коли ти не зі мною, стає набагато важчим. Моє серце б'ється лише за тобою, і я дуже сумую."
    "Ти завжди була для мене опорою і найкращим другом. Немає дня, коли я не думаю про тебе та той момент, коли знову буду біля тебе. Ти - моє світло, яке освітлює мій шлях, і я не можу дочекатися того дня, коли це світло знову освітить моє життя."
    "Щоби ми були разом, мені доведеться виїхати в невелике відрядження. Я залишу місто 17 липня і повернуся назад в кінці місяця. Обіцяю, що ця розлука зміцнить наше кохання і наш зв'язок. Незважаючи на відстань, ми завжди поруч. Скоро ми знову будемо разом, і я зможу тримати тебе в своїх обіймах."
    "З любов'ю, \n Томас"

    "Максвел, прочитавши цей діалог, почув дивний звук, повернувши дзеркало, він побачив  карточку, на якій написано '17'"

    m "Що за...? Неллі, чула цей дивний звук? І подивись, що я тут знайшов. Напис з числом '17'. Як воно пов'язане з усім цим?"

    show nelli_thinking_hands_behind
    n "Думаю, це число пов'язане з листом. Томас писав, що він вирушає у відрядження 17 липня. Можливо, це той момент, коли він туди поїхав."
    hide nelli_thinking_hands_behind

menu:
        "Погодитись":
            jump choices4_a
        "Заперечити":
            jump choices4_b

label choices4_a:
        m "Можливо, ти маєш рацію. Здається, що це число - ключ до подальшого розвитку подій. Можливо, нам варто докладніше розглянути це та з'ясувати, що воно нам розкаже."

        show nelli neutral
        n "Він точно містить ключову інформацію."
        hide nelli neutral
        jump choices4_common

label choices4_b:
        m "Неллі, це все маячня. Я не вірю в ці загадки та числа. Можливо, це випадковість, і нам не варто витрачати час на це."

        show nelli_thinking_hands_straight
        n "Але це так дивно, що це число відповідає даті відрядження Томаса. Можливо, у цьому є якась важлива інформація, яку ми поки не розуміємо."
        hide nelli_thinking_hands_straight
        jump choices4_common

label choices4_common:
    show bob_straight3
    bob "Дивіться, тепер після вирішення цієї загадки я можу зсунути прохід в іншу кімнату!"
    hide bob_straight3
    #[Відкривається прохід далі, перший вирушає БОБ]
    #\3 локація:\
    scene bg location3 with fade
    show bob_straight2
    bob "Не гайте часу, заходьте швидше. Загадки чекають на нас!"
    hide bob_straight2
    #(Ліхтарик гасне)
    m "Не можу ввімкнути фонарик Боба. Схоже, заряд батарейки закінчився."
    nn "???"
    m "Дивні звуки... Схожі на схлипування. Це чули всі, чи це тільки в моїй голові?"
    show nelli_neutral_arms_on_belt
    n "Тут щось не так, будемо обережнішими."
    hide nelli_neutral_arms_on_belt
    show bob_straight4
    bob "Аго-ов, тут є хто?"
    hide bob_straight4
    m "Я думаю, тут є хтось крім нас. Краще не кричи."
    show bob_straight2
    bob "Навіть якщо є, я йому так смачно наваляю! Ви лише покладіться на мене."
    hide bob_straight2

    #[Звук, який чув Максвел, став на багато голоснішим.]
    m "Неллі!"

    #[Максвел швидко хапає Неллі і вони ховаються за стіною]
    #\Відрізаний крик Боба\
    play sound scream
    m "(в думках) Коли я почув останній крик Боба, час перестав йти для мене."
    m "(в думках) Я боявся видавати звуки, навіть дихання. Мені було дуже страшно."
    stop sound
    m "(в думках) В мить я подумав, що вже розстався зі своїм життям, як і Боб. Я ніби-то випав з реальності."
    m "(в думках) Я вже почав уявляти, що відбулось з Бобом, але з цього стану мене витянула Неллі, котра товкала мене в плече."
    m "(в думках) Ще деякий час я просто дивився на неї. На її лиці був страх і нерозуміння."
    m "(в думках) Коли я зрозумів, що щось потрібно робити, я ввімкнув свій ліхтарик, взяв Неллі за руку і потягнув в попередню локацію."
    m "(в думках) В мить вона зупинилась і почала дивитись на землю перед входом в кімнату."
    m "(в думках) Я подивився туди ж та побачив розбризкану чорну рідину..."

    "The end"
return
