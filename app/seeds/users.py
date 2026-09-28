from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_users():
    user1 = User(
        username='AliceWonder1',
        email='alice@wonderland.ioo',
        first_name='Alice',
        last_name='Wonder',
        password='passwordAlice',
        address='123 Wonderland St',
        phone='123-456-7890',
        profile_image_id="https://robohash.org/1",
        # role='admin',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    user2 = User(
        username='BobBuilder1',
        email='bob@builder.io0',
        first_name='Bob',
        last_name='Builder',
        password='passwordBob',
        address='456 Construct Ave',
        phone='987-654-3210',
        profile_image_id="https://robohash.org/2",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    user3 = User(
        username='CharlieChocolate',
        email='charlie@choco.io',
        first_name='Charlie',
        last_name='Chocolate',
        password='passwordCharlie',
        address='789 Choco Blvd',
        phone='123-789-4560',
        profile_image_id="https://robohash.org/3",
        # role='admin',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    user4 = User(
        username='DavidDreamer',
        email='david@dream.io',
        first_name='David',
        last_name='Dreamer',
        password='passwordDavid',
        address='012 Dream Way',
        phone='456-123-7890',
        profile_image_id="https://robohash.org/4",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    user5 = User(
        username='EvaExplorer',
        email='eva@explore.io',
        first_name='Eva',
        last_name='Explorer',
        password='passwordEva',
        address='345 Explore Rd',
        phone='789-123-4560',
        profile_image_id="https://robohash.org/5",
        # role='admin',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    tobe_ornottobe = User(
        username='youguessedit',
        email='englishwriter@user.io',
        first_name='Tobe',
        last_name='Ornottobe',
        password='password6',
        address='123 Choco Blvd',
        phone='202-555-0101',
        profile_image_id="https://robohash.org/6",
        # role='admin',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    stu_dent = User(
        username='studybuddy',
        email='hitthebooks@user.io',
        first_name='Stu',
        last_name='Dent',
        password='password7',
        address='611 Tangerine Way',
        phone='341-555-0161',
        profile_image_id="https://robohash.org/7",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ali_bye = User(
        username='seeyoulater',
        email='farewellgreetings@goodbyes.io',
        first_name='Ali',
        last_name='Bye',
        password='password8',
        address='622 Lime Ave',
        phone='342-555-0162',
        profile_image_id="https://robohash.org/8",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    sandy_shore = User(
        username='beachlover',
        email='waves@coastal.io',
        first_name='Sandy',
        last_name='Shore',
        password='password102',
        address='633 Mango St',
        phone='343-555-0163',
        profile_image_id="https://robohash.org/9",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    phil_up = User(
        username='gasstationguy',
        email='fuel@tank.io',
        first_name='Phil',
        last_name='Up',
        password='password103',
        address='644 Papaya Dr',
        phone='344-555-0164',
        profile_image_id="https://robohash.org/10",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    barry_dalive = User(
        username='graveyardshift',
        email='spooky@crypt.io',
        first_name='Barry',
        last_name='Dalive',
        password='password104',
        address='655 Grape Blvd',
        phone='345-555-0165',
        profile_image_id="https://robohash.org/11",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    holly_wood = User(
        username='filmstar',
        email='movies@la.io',
        first_name='Holly',
        last_name='Wood',
        password='password105',
        address='666 Olive Ln',
        phone='346-555-0166',
        profile_image_id="https://robohash.org/12",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    chris_pbacon = User(
        username='morningmeal',
        email='breakfast@meal.io',
        first_name='Chris',
        last_name='PBacon',
        password='password106',
        address='677 Peach Pl',
        phone='347-555-0167',
        profile_image_id="https://robohash.org/13",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    terry_bull = User(
        username='notsogood',
        email='warning@caution.io',
        first_name='Terry',
        last_name='Bull',
        password='password107',
        address='688 Pecan Rd',
        phone='348-555-0168',
        profile_image_id="https://robohash.org/14",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    anita_bath = User(
        username='cleanclean',
        email='hygiene@wash.io',
        first_name='Anita',
        last_name='Bath',
        password='password108',
        address='699 Fig St',
        phone='349-555-0169',
        profile_image_id="https://robohash.org/15",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    carmen_getit = User(
        username='quickshopper',
        email='fast@buy.io',
        first_name='Carmen',
        last_name='Getit',
        password='password109',
        address='7001 Cashew Ave',
        phone='350-555-0170',
        profile_image_id="https://robohash.org/16",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    walter_fall = User(
        username='naturelover',
        email='scenic@hike.io',
        first_name='Walter',
        last_name='Fall',
        password='password110',
        address='711 Cherry Dr',
        phone='351-555-0171',
        profile_image_id="https://robohash.org/17",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    willie_makeit = User(
        username='determined',
        email='goals@achieve.io',
        first_name='Willie',
        last_name='Makeit',
        password='password111',
        address='722 Pear Rd',
        phone='352-555-0172',
        profile_image_id="https://robohash.org/18",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    al_igator = User(
        username='swampguy',
        email='reptile@bayou.io',
        first_name='Al',
        last_name='Igator',
        password='password112',
        address='733 Apricot Blvd',
        phone='353-555-0173',
        profile_image_id="https://robohash.org/19",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ella_phant = User(
        username='bigandgentle',
        email='safari@zoo.io',
        first_name='Ella',
        last_name='Phant',
        password='password113',
        address='744 Raspberry Ln',
        phone='354-555-0174',
        profile_image_id="https://robohash.org/20",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ian_flatable = User(
        username='airfilled',
        email='balloons@party.io',
        first_name='Ian',
        last_name='Flatable',
        password='password114',
        address='755 Apple St',
        phone='355-555-0175',
        profile_image_id="https://robohash.org/21",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    norm_al = User(
        username='averagejoe',
        email='regular@everyday.io',
        first_name='Norm',
        last_name='Al',
        password='password115',
        address='766 Guava Dr',
        phone='356-555-0176',
        profile_image_id="https://robohash.org/22",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    catie_pillar = User(
        username='slowmover',
        email='nature@bugs.io',
        first_name='Catie',
        last_name='Pillar',
        password='password116',
        address='777 Nectarine Blvd',
        phone='357-555-0177',
        profile_image_id="https://robohash.org/23",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    rob_ank = User(
        username='bankerguy',
        email='money@savings.io',
        first_name='Rob',
        last_name='Ank',
        password='password117',
        address='788 Passionfruit Ln',
        phone='358-555-0178',
        profile_image_id="https://robohash.org/24",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    joy_stick = User(
        username='gamerpro',
        email='games@console.io',
        first_name='Joy',
        last_name='Stick',
        password='password118',
        address='799 Lychee Pl',
        phone='359-555-0179',
        profile_image_id="https://robohash.org/25",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    mary_go = User(
        username='funpark',
        email='roundandround@play.io',
        first_name='Mary',
        last_name='Go',
        password='password119',
        address='8010 Kiwi Rd',
        phone='360-555-0180',
        profile_image_id="https://robohash.org/26",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    tina_bopper = User(
        username='dancefloor',
        email='music@party.io',
        first_name='Tina',
        last_name='Bopper',
        password='password120',
        address='812 Pineapple Ave',
        phone='361-555-0181',
        profile_image_id="https://robohash.org/27",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ian_tense = User(
        username='seriousguy',
        email='focus@work.io',
        first_name='Ian',
        last_name='Tense',
        password='password121',
        address='823 Banana Dr',
        phone='362-555-0182',
        profile_image_id="https://robohash.org/28",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    jill_out = User(
        username='relaxer',
        email='chill@relax.io',
        first_name='Jill',
        last_name='Out',
        password='password122',
        address='834 Watermelon Way',
        phone='363-555-0183',
        profile_image_id="https://robohash.org/29",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    art_ist = User(
        username='paintsbrushes',
        email='canvas@studio.io',
        first_name='Art',
        last_name='Ist',
        password='password123',
        address='845 Cantaloupe St',
        phone='364-555-0184',
        profile_image_id="https://robohash.org/30",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    rob_inhood = User(
        username='sherwood',
        email='arrow@archer.io',
        first_name='Rob',
        last_name='Inhood',
        password='password124',
        address='856 Honeydew Dr',
        phone='365-555-0185',
        profile_image_id="https://robohash.org/31",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ella_vate = User(
        username='upanddown',
        email='lift@elevator.io',
        first_name='Ella',
        last_name='Vate',
        password='password125',
        address='867 Guava Blvd',
        phone='366-555-0186',
        profile_image_id="https://robohash.org/32",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    andy_gravity = User(
        username='flyhigh',
        email='space@nasa.io',
        first_name='Andy',
        last_name='Gravity',
        password='password126',
        address='878 Plum Ln',
        phone='367-555-0187',
        profile_image_id="https://robohash.org/33",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    anne_tenna = User(
        username='signalboost',
        email='radio@broadcast.io',
        first_name='Anne',
        last_name='Tenna',
        password='password127',
        address='889 Avocado Pl',
        phone='368-555-0188',
        profile_image_id="https://robohash.org/34",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    will_power = User(
        username='determination',
        email='motivation@success.io',
        first_name='Will',
        last_name='Power',
        password='password128',
        address='8910 Dragonfruit Rd',
        phone='369-555-0189',
        profile_image_id="https://robohash.org/35",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    luke_out = User(
        username='looker',
        email='vision@watch.io',
        first_name='Luke',
        last_name='Out',
        password='password129',
        address='9021 Pine St',
        phone='370-555-0190',
        profile_image_id="https://robohash.org/36",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    sue_perb = User(
        username='exceptional',
        email='quality@best.io',
        first_name='Sue',
        last_name='Perb',
        password='password130',
        address='9199 Cedar Ave',
        phone='371-555-0991',
        profile_image_id="https://robohash.org/37",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ivan_idea = User(
        username='thinktank',
        email='brain@innovate.io',
        first_name='Ivan',
        last_name='Idea',
        password='password131',
        address='9132 Cedar Ave',
        phone='371-555-0191',
        profile_image_id="https://robohash.org/38",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    drew_paper = User(
        username='sketchbook',
        email='art@draw.io',
        first_name='Drew',
        last_name='Paper',
        password='password132',
        address='9243 Maple Dr',
        phone='372-555-0192',
        profile_image_id="https://robohash.org/39",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    justin_time = User(
        username='alwaysontime',
        email='clock@timely.io',
        first_name='Justin',
        last_name='Time',
        password='password133',
        address='9354 Redwood Blvd',
        phone='373-555-0193',
        profile_image_id="https://robohash.org/40",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    pat_down = User(
        username='security',
        email='check@airport.io',
        first_name='Pat',
        last_name='Down',
        password='password134',
        address='9465 Willow Ln',
        phone='374-555-0194',
        profile_image_id="https://robohash.org/41",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    sonny_day = User(
        username='weatherman',
        email='forecast@shine.io',
        first_name='Sonny',
        last_name='Day',
        password='password135',
        address='9576 Birch St',
        phone='375-555-0195',
        profile_image_id="https://robohash.org/42",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    neil_down = User(
        username='devotee',
        email='pray@temple.io',
        first_name='Neil',
        last_name='Down',
        password='password136',
        address='9687 Elm Dr',
        phone='376-555-0196',
        profile_image_id="https://robohash.org/43",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    bill_board = User(
        username='signmaker',
        email='advertise@ads.io',
        first_name='Bill',
        last_name='Board',
        password='password137',
        address='9798 Oak Way',
        phone='377-555-0197',
        profile_image_id="https://robohash.org/44",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    may_flowers = User(
        username='gardener1',
        email='bloom1@spring.io',
        first_name='Mayl',
        last_name='Flowers',
        password='password1381',
        address='98109 Fir Rd',
        phone='378-555-0198',
        profile_image_id="https://robohash.org/45",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    stan_dup = User(
        username='comedian',
        email='jokes@laugh.io',
        first_name='Stan',
        last_name='Dup',
        password='password139',
        address='100120 Alder Blvd',
        phone='379-555-0199',
        profile_image_id="https://robohash.org/46",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    dee_veloper = User(
    username='codegeek',
    email='dee@codebase.io',
    first_name='Dee',
    last_name='Veloper',
    password='password142',
    address='101131 Spruce Ln',
    phone='380-555-0200',
    profile_image_id="https://robohash.org/47",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    tim_ber = User(
    username='treehugger',
    email='tim@forest.io',
    first_name='Tim',
    last_name='Ber',
    password='password143',
    address='1012 Hazel St',
    phone='381-555-0201',
    profile_image_id="https://robohash.org/48",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    may_day = User(
    username='emergency',
    email='may@alert.io',
    first_name='May',
    last_name='Day',
    password='password144',
    address='1023 Pinecone Ave',
    phone='382-555-0202',
    profile_image_id="https://robohash.org/49",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    glen_cove = User(
    username='naturalscenery',
    email='glen@landscape.io',
    first_name='Glen',
    last_name='Cove',
    password='password145',
    address='1034 Cypress Blvd',
    phone='383-555-0203',
    profile_image_id="https://robohash.org/50",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    hal_lowed = User(
    username='holyman',
    email='hal@sanctuary.io',
    first_name='Hal',
    last_name='Lowed',
    password='password146',
    address='1045 Redbud Ln',
    phone='384-555-0204',
    profile_image_id="https://robohash.org/51",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    sam_wich = User(
    username='foodlover',
    email='sam@deli.io',
    first_name='Sam',
    last_name='Wich',
    password='password147',
    address='1056 Dogwood Dr',
    phone='385-555-0205',
    profile_image_id="https://robohash.org/52",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    earl_ybird = User(
    username='morningperson',
    email='earl@sunrise.io',
    first_name='Earl',
    last_name='Ybird',
    password='password148',
    address='1067 Sequoia Way',
    phone='386-555-0206',
    profile_image_id="https://robohash.org/53",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    rose_bud = User(
    username='gardener',
    email='rose@floral.io',
    first_name='Rose',
    last_name='Bud',
    password='password149',
    address='1078 Cedarbark Rd',
    phone='387-555-0207',
    profile_image_id="https://robohash.org/54",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    ted_ebear = User(
    username='cuddlebuddy',
    email='ted@toys.io',
    first_name='Ted',
    last_name='Ebear',
    password='password150',
    address='1089 Teakwood Pl',
    phone='388-555-0208',
    profile_image_id="https://robohash.org/55",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    ella_vate = User(
    username='lifter',
    email='ella@machines.io',
    first_name='Ella',
    last_name='Vate',
    password='password151',
    address='10910 Magnolia Blvd',
    phone='389-555-0209',
    profile_image_id="https://robohash.org/56",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    clara_net = User(
    username='musician',
    email='clara@band.io',
    first_name='Clara',
    last_name='Net',
    password='password152',
    address='11021 Tulip Dr',
    phone='390-555-0210',
    profile_image_id="https://robohash.org/57",
    #  role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    violin_tunes = User(
    username='stringplayer',
    email='violin@orchestra.io',
    first_name='Viola',
    last_name='Tunes',
    password='password153',
    address='11132 Rose Ln',
    phone='391-555-0211',
    profile_image_id="https://robohash.org/58",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    lee_der = User(
    username='headofthepack',
    email='lee@groups.io',
    first_name='Lee',
    last_name='Der',
    password='password154',
    address='11243 Daffodil Rd',
    phone='392-555-0212',
    profile_image_id="https://robohash.org/59",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    crystal_ball = User(
    username='seer',
    email='crystal@future.io',
    first_name='Crystal',
    last_name='Ball',
    password='password155',
    address='11354 Sunflower St',
    phone='393-555-0213',
    profile_image_id="https://robohash.org/60",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    jenny_rator = User(
    username='poweruser',
    email='jenny@energy.io',
    first_name='Jenny',
    last_name='Rator',
    password='password156',
    address='11465 Violet Ave',
    phone='394-555-0214',
    profile_image_id="https://robohash.org/61",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    perry_odic = User(
    username='scientist',
    email='perry@elements.io',
    first_name='Perry',
    last_name='Odic',
    password='password157',
    address='11576 Daisy Dr',
    phone='395-555-0215',
    profile_image_id="https://robohash.org/62",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    sue_pernova = User(
    username='astronomer',
    email='sue@stars.io',
    first_name='Sue',
    last_name='Pernova',
    password='password158',
    address='11687 Marigold Blvd',
    phone='396-555-0216',
    profile_image_id="https://robohash.org/63",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    anna_lytics = User(
    username='dataanalyst',
    email='anna@data.io',
    first_name='Anna',
    last_name='Lytics',
    password='password159',
    address='11798 Lilac Ln',
    phone='397-555-0217',
    profile_image_id="https://robohash.org/64",
    # role='user',
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)
    olive_branch = User(
        username='peacemaker',
        email='reconciliation@harmony.io',
        first_name='Olive',
        last_name='Branch',
        password='password140',
        address='118109 Orchid Rd',
        phone='398-555-0218',
        profile_image_id="https://robohash.org/65",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ella_ment = User(
        username='basic',
        email='foundations@roots.io',
        first_name='Ella',
        last_name='Ment',
        password='password141',
        address='119120 Jasmine Pl',
        phone='399-555-0219',
        profile_image_id="https://robohash.org/66",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    earl_gray = User(
        username='tealover',
        email='brew@teapot.io',
        first_name='Earl',
        last_name='Gray',
        password='password142',
        address='120131 Lavender St',
        phone='400-555-0220',
        profile_image_id="https://robohash.org/67",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    jack_pot = User(
        username='luckyone',
        email='winner@casino.io',
        first_name='Jack',
        last_name='Pot',
        password='password143',
        address='121142 Gardenia Way',
        phone='401-555-0221',
        profile_image_id="https://robohash.org/68",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    moe_tion = User(
        username='onmove',
        email='dynamics@flow.io',
        first_name='Moe',
        last_name='Tion',
        password='password144',
        address='122153 Peony Dr',
        phone='402-555-0222',
        profile_image_id="https://robohash.org/69",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    dale_ivery = User(
        username='fastservice',
        email='shipping@deliver.io',
        first_name='Dale',
        last_name='Ivery',
        password='password145',
        address='123164 Poppy Ln',
        phone='403-555-0223',
        profile_image_id="https://robohash.org/70",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    pat_riotic = User(
        username='proudlocal',
        email='pride@nation.io',
        first_name='Pat',
        last_name='Riotic',
        password='password146',
        address='124175 Iris Ave',
        phone='404-555-0224',
        profile_image_id="https://robohash.org/71",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    jenny_rate = User(
        username='powerhouse',
        email='energy@produce.io',
        first_name='Jenny',
        last_name='Rate',
        password='password147',
        address='125186 Hydrangea Blvd',
        phone='405-555-0225',
        profile_image_id="https://robohash.org/72",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    rocky_road = User(
        username='icecreamlover',
        email='sweets@dessert.io',
        first_name='Rocky',
        last_name='Road',
        password='password148',
        address='126197 Zinnia Rd',
        phone='406-555-0226',
        profile_image_id="https://robohash.org/73",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    steve_adore = User(
        username='entrancelover',
        email='welcome@doors.io',
        first_name='Steve',
        last_name='Adore',
        password='password149',
        address='127888 Aster St',
        phone='407-555-9999',
        profile_image_id="https://robohash.org/74",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ty_tanic = User(
        username='bigship',
        email='ocean@vessel.io',
        first_name='Ty',
        last_name='Tanic',
        password='password150',
        address='127208 Aster St',
        phone='407-555-0227',
        profile_image_id="https://robohash.org/75",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    liz_tening = User(
        username='goodlistener',
        email='hearing@conversations.io',
        first_name='Liz',
        last_name='Tening',
        password='password151',
        address='128219 Lily Dr',
        phone='408-555-0228',
        profile_image_id="https://robohash.org/76",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    tom_orrow = User(
        username='planner',
        email='future@scheduled.io',
        first_name='Tom',
        last_name='Orrow',
        password='password152',
        address='129230 Pansy Ln',
        phone='409-555-0229',
        profile_image_id="https://robohash.org/77",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ann_chovy = User(
        username='pizzaaddict',
        email='toppings@pizza.io',
        first_name='Ann',
        last_name='Chovy',
        password='password153',
        address='130241 Tulip Ave',
        phone='410-555-0230',
        profile_image_id="https://robohash.org/78",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    frank_furter = User(
        username='hotdoglover',
        email='grill@bbq.io',
        first_name='Frank',
        last_name='Furter',
        password='password154',
        address='131252 Daisy Blvd',
        phone='411-555-0231',
        profile_image_id="https://robohash.org/79",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ray_sing = User(
        username='trackstar',
        email='speed@racetrack.io',
        first_name='Ray',
        last_name='Sing',
        password='password155',
        address='132263 Daffodil Rd',
        phone='412-555-0232',
        profile_image_id="https://robohash.org/80",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    daisy_chain = User(
        username='flowerfan',
        email='blossom@garden.io',
        first_name='Daisy',
        last_name='Chain',
        password='password156',
        address='133274 Buttercup Dr',
        phone='413-555-0233',
        profile_image_id="https://robohash.org/81",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    brad_crumb = User(
        username='breadlover',
        email='baker@bakery.io',
        first_name='Brad',
        last_name='Crumb',
        password='password157',
        address='134285 Snowdrop Ln',
        phone='414-555-0234',
        profile_image_id="https://robohash.org/82",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    rose_bush = User(
        username='gardeningpro',
        email='flowers@botany.io',
        first_name='Rose',
        last_name='Bush',
        password='password152',
        address='135296 Primrose Ave',
        phone='415-555-0235',
        profile_image_id="https://robohash.org/83",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    chip_munk = User(
        username='nutsforlife',
        email='acorns@forest.io',
        first_name='Chip',
        last_name='Munk',
        password='password153',
        address='136307 Bluebell Way',
        phone='416-555-0236',
        profile_image_id="https://robohash.org/84",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    cliff_hanger = User(
        username='suspenseking',
        email='stories@adventure.io',
        first_name='Cliff',
        last_name='Hanger',
        password='password154',
        address='137318 Begonia Dr',
        phone='417-555-0237',
        profile_image_id="https://robohash.org/85",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    wendy_wind = User(
        username='breezygirl',
        email='air@atmosphere.io',
        first_name='Wendy',
        last_name='Wind',
        password='password155',
        address='138329 Hibiscus Blvd',
        phone='418-555-0238',
        profile_image_id="https://robohash.org/86",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    cole_dmine = User(
        username='deepdigger',
        email='ore@mine.io',
        first_name='Cole',
        last_name='Dmine',
        password='password156',
        address='139340 Azalea Ln',
        phone='419-555-0239',
        profile_image_id="https://robohash.org/87",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    rocky_shore = User(
        username='oceanicman',
        email='waves@beach.io',
        first_name='Rocky',
        last_name='Shore',
        password='password157',
        address='140351 Freesia Rd',
        phone='420-555-0240',
        profile_image_id="https://robohash.org/88",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    crystal_ball = User(
        username='fortuneteller',
        email='future@predict.io',
        first_name='Crystal',
        last_name='Ball',
        password='password158',
        address='141362 Camellia Blvd',
        phone='421-555-0241',
        profile_image_id="https://robohash.org/89",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    sandy_beach = User(
        username='sunandsea',
        email='tides@ocean.io',
        first_name='Sandy',
        last_name='Beach',
        password='password159',
        address='142373 Dandelion Dr',
        phone='422-555-0242',
        profile_image_id="https://robohash.org/90",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    bill_folds = User(
        username='walletman',
        email='cash@money.io',
        first_name='Bill',
        last_name='Folds',
        password='password160',
        address='143384 Sunflower Ln',
        phone='423-555-0243',
        profile_image_id="https://robohash.org/91",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    terri_bull = User(
        username='monstermovies',
        email='horror@cinema.io',
        first_name='Terri',
        last_name='Bull',
        password='password161',
        address='144395 Petunia Ave',
        phone='424-555-0244',
        profile_image_id="https://robohash.org/92",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    barbie_cue = User(
        username='grillmaster',
        email='cooking@bbq.io',
        first_name='Barbie',
        last_name='Cue',
        password='password162',
        address='145406 Marigold St',
        phone='425-555-0245',
        profile_image_id="https://robohash.org/93",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    ty_tan = User(
        username='giantfan',
        email='legends@myth.io',
        first_name='Ty',
        last_name='Tan',
        password='password163',
        address='146417 Snapdragon Rd',
        phone='426-555-0246',
        profile_image_id="https://robohash.org/94",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    lou_minate = User(
        username='shinebright',
        email='lights@glow.io',
        first_name='Lou',
        last_name='Minate',
        password='password164',
        address='147428 Dahlia Way',
        phone='427-555-0247',
        profile_image_id="https://robohash.org/95",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    holly_day = User(
        username='festivegirl',
        email='celebrate@events.io',
        first_name='Holly',
        last_name='Day',
        password='password165',
        address='148439 Lotus Ln',
        phone='428-555-0248',
        profile_image_id="https://robohash.org/96",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    phil_ter = User(
        username='cleanwater',
        email='purify@eco.io',
        first_name='Phil',
        last_name='Ter',
        password='password166',
        address='149440 Chrysanthemum Blvd',
        phone='429-555-0249',
        profile_image_id="https://robohash.org/97",
        # role='user',
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.session.add_all([user1, user2, user3, user4, user5,
    tobe_ornottobe, stu_dent, ali_bye, sandy_shore,
    phil_up, barry_dalive, holly_wood, chris_pbacon,
    terry_bull, anita_bath, carmen_getit, walter_fall,
    willie_makeit, al_igator, ella_phant, ian_flatable,
    norm_al, catie_pillar, rob_ank, joy_stick, mary_go,
    tina_bopper, ian_tense, dee_veloper, tim_ber, may_day,
    glen_cove, hal_lowed, sam_wich, earl_ybird, rose_bud,
    ted_ebear, ella_vate, clara_net, violin_tunes, lee_der,
    crystal_ball, jenny_rator, perry_odic, sue_pernova,
    anna_lytics,jill_out, art_ist, rob_inhood,
    ella_vate, andy_gravity, anne_tenna, will_power,
    luke_out, sue_perb, ivan_idea, drew_paper, justin_time,
    pat_down, sonny_day, neil_down, bill_board, may_flowers, stan_dup,
    olive_branch, ella_ment, earl_gray, jack_pot, moe_tion,
    dale_ivery, pat_riotic, jenny_rate, rocky_road, steve_adore,
    ty_tanic, liz_tening, tom_orrow, ann_chovy, frank_furter,
    ray_sing, daisy_chain, brad_crumb, rose_bush, chip_munk, cliff_hanger, wendy_wind, cole_dmine,
    rocky_shore, crystal_ball, sandy_beach, bill_folds,
    terri_bull, barbie_cue, ty_tan, lou_minate, holly_day, phil_ter])

    # db.session.add_all([brad_crumb, rose_bush, chip_munk, cliff_hanger, wendy_wind, cole_dmine,
    # rocky_shore, crystal_ball, sandy_beach, bill_folds,
    # terri_bull, barbie_cue, ty_tan, lou_minate, holly_day, phil_ter])

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
