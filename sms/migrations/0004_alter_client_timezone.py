# Generated by Django 4.2.3 on 2023-07-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_alter_client_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='timezone',
            field=models.CharField(choices=[('Pacific/Johnston', 'Pacific/Johnston'), ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'), ('America/Ciudad_Juarez', 'America/Ciudad_Juarez'), ('US/Central', 'US/Central'), ('Europe/Busingen', 'Europe/Busingen'), ('Africa/Douala', 'Africa/Douala'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Europe/Zaporozhye', 'Europe/Zaporozhye'), ('Asia/Kabul', 'Asia/Kabul'), ('America/Fortaleza', 'America/Fortaleza'), ('America/Bogota', 'America/Bogota'), ('America/Mendoza', 'America/Mendoza'), ('Africa/Bangui', 'Africa/Bangui'), ('Africa/Bamako', 'Africa/Bamako'), ('Pacific/Tahiti', 'Pacific/Tahiti'), ('Pacific/Palau', 'Pacific/Palau'), ('Asia/Ust-Nera', 'Asia/Ust-Nera'), ('America/Bahia', 'America/Bahia'), ('NZ-CHAT', 'NZ-CHAT'), ('America/Boa_Vista', 'America/Boa_Vista'), ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'), ('Atlantic/St_Helena', 'Atlantic/St_Helena'), ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'), ('Asia/Chita', 'Asia/Chita'), ('America/Iqaluit', 'America/Iqaluit'), ('America/Glace_Bay', 'America/Glace_Bay'), ('Pacific/Yap', 'Pacific/Yap'), ('Etc/GMT+12', 'Etc/GMT+12'), ('Europe/Kirov', 'Europe/Kirov'), ('America/Danmarkshavn', 'America/Danmarkshavn'), ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'), ('Australia/Tasmania', 'Australia/Tasmania'), ('Asia/Almaty', 'Asia/Almaty'), ('Atlantic/Faroe', 'Atlantic/Faroe'), ('America/Eirunepe', 'America/Eirunepe'), ('Europe/Nicosia', 'Europe/Nicosia'), ('Africa/Maseru', 'Africa/Maseru'), ('Pacific/Samoa', 'Pacific/Samoa'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Etc/GMT-0', 'Etc/GMT-0'), ('America/Winnipeg', 'America/Winnipeg'), ('Asia/Damascus', 'Asia/Damascus'), ('America/Swift_Current', 'America/Swift_Current'), ('Pacific/Efate', 'Pacific/Efate'), ('Asia/Manila', 'Asia/Manila'), ('America/Santarem', 'America/Santarem'), ('Jamaica', 'Jamaica'), ('America/Nassau', 'America/Nassau'), ('America/Rankin_Inlet', 'America/Rankin_Inlet'), ('Europe/Moscow', 'Europe/Moscow'), ('America/Cayman', 'America/Cayman'), ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'), ('America/Maceio', 'America/Maceio'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Africa/Lome', 'Africa/Lome'), ('GMT', 'GMT'), ('Pacific/Kanton', 'Pacific/Kanton'), ('America/St_Thomas', 'America/St_Thomas'), ('America/Shiprock', 'America/Shiprock'), ('Antarctica/Davis', 'Antarctica/Davis'), ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'), ('America/Nuuk', 'America/Nuuk'), ('America/Vancouver', 'America/Vancouver'), ('America/Grand_Turk', 'America/Grand_Turk'), ('Europe/Athens', 'Europe/Athens'), ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Europe/Belfast', 'Europe/Belfast'), ('US/Eastern', 'US/Eastern'), ('Iran', 'Iran'), ('Canada/Saskatchewan', 'Canada/Saskatchewan'), ('Europe/Andorra', 'Europe/Andorra'), ('Africa/Libreville', 'Africa/Libreville'), ('Europe/Samara', 'Europe/Samara'), ('Etc/GMT+0', 'Etc/GMT+0'), ('America/Asuncion', 'America/Asuncion'), ('Etc/Zulu', 'Etc/Zulu'), ('America/Moncton', 'America/Moncton'), ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'), ('ROC', 'ROC'), ('Asia/Omsk', 'Asia/Omsk'), ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'), ('Asia/Chungking', 'Asia/Chungking'), ('Asia/Bahrain', 'Asia/Bahrain'), ('America/Guayaquil', 'America/Guayaquil'), ('America/Tegucigalpa', 'America/Tegucigalpa'), ('America/Menominee', 'America/Menominee'), ('W-SU', 'W-SU'), ('America/Porto_Velho', 'America/Porto_Velho'), ('Hongkong', 'Hongkong'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('America/Chicago', 'America/Chicago'), ('Pacific/Saipan', 'Pacific/Saipan'), ('America/Merida', 'America/Merida'), ('America/Martinique', 'America/Martinique'), ('Poland', 'Poland'), ('Africa/Monrovia', 'Africa/Monrovia'), ('Asia/Shanghai', 'Asia/Shanghai'), ('America/Virgin', 'America/Virgin'), ('Asia/Rangoon', 'Asia/Rangoon'), ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'), ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'), ('Asia/Aden', 'Asia/Aden'), ('Singapore', 'Singapore'), ('America/Porto_Acre', 'America/Porto_Acre'), ('Asia/Karachi', 'Asia/Karachi'), ('America/Buenos_Aires', 'America/Buenos_Aires'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Asia/Calcutta', 'Asia/Calcutta'), ('localtime', 'localtime'), ('America/North_Dakota/Center', 'America/North_Dakota/Center'), ('Etc/GMT-13', 'Etc/GMT-13'), ('Europe/Brussels', 'Europe/Brussels'), ('America/La_Paz', 'America/La_Paz'), ('America/Noronha', 'America/Noronha'), ('Canada/Yukon', 'Canada/Yukon'), ('NZ', 'NZ'), ('Asia/Thimphu', 'Asia/Thimphu'), ('Africa/Mogadishu', 'Africa/Mogadishu'), ('Indian/Kerguelen', 'Indian/Kerguelen'), ('Europe/Oslo', 'Europe/Oslo'), ('Asia/Colombo', 'Asia/Colombo'), ('Indian/Christmas', 'Indian/Christmas'), ('Africa/Niamey', 'Africa/Niamey'), ('America/Whitehorse', 'America/Whitehorse'), ('Antarctica/Vostok', 'Antarctica/Vostok'), ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'), ('MST', 'MST'), ('Cuba', 'Cuba'), ('America/Yellowknife', 'America/Yellowknife'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Asia/Saigon', 'Asia/Saigon'), ('Pacific/Noumea', 'Pacific/Noumea'), ('Pacific/Fiji', 'Pacific/Fiji'), ('Pacific/Nauru', 'Pacific/Nauru'), ('Asia/Makassar', 'Asia/Makassar'), ('America/Anchorage', 'America/Anchorage'), ('America/Araguaina', 'America/Araguaina'), ('America/Paramaribo', 'America/Paramaribo'), ('Europe/Monaco', 'Europe/Monaco'), ('Asia/Tomsk', 'Asia/Tomsk'), ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'), ('Asia/Bangkok', 'Asia/Bangkok'), ('America/Manaus', 'America/Manaus'), ('Pacific/Ponape', 'Pacific/Ponape'), ('Africa/Lubumbashi', 'Africa/Lubumbashi'), ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'), ('America/Matamoros', 'America/Matamoros'), ('Africa/Malabo', 'Africa/Malabo'), ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'), ('Etc/GMT-4', 'Etc/GMT-4'), ('CST6CDT', 'CST6CDT'), ('Asia/Muscat', 'Asia/Muscat'), ('Australia/Adelaide', 'Australia/Adelaide'), ('America/Indiana/Winamac', 'America/Indiana/Winamac'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Etc/GMT+5', 'Etc/GMT+5'), ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'), ('Africa/Maputo', 'Africa/Maputo'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('America/Santo_Domingo', 'America/Santo_Domingo'), ('Asia/Qyzylorda', 'Asia/Qyzylorda'), ('Etc/GMT0', 'Etc/GMT0'), ('HST', 'HST'), ('Atlantic/Madeira', 'Atlantic/Madeira'), ('Etc/Greenwich', 'Etc/Greenwich'), ('America/Atka', 'America/Atka'), ('Australia/Brisbane', 'Australia/Brisbane'), ('Etc/GMT-11', 'Etc/GMT-11'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Europe/Skopje', 'Europe/Skopje'), ('America/Panama', 'America/Panama'), ('Canada/Eastern', 'Canada/Eastern'), ('Etc/UCT', 'Etc/UCT'), ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'), ('Africa/Tunis', 'Africa/Tunis'), ('America/Jujuy', 'America/Jujuy'), ('Africa/Dakar', 'Africa/Dakar'), ('WET', 'WET'), ('Pacific/Kiritimati', 'Pacific/Kiritimati'), ('Australia/Broken_Hill', 'Australia/Broken_Hill'), ('Europe/Tallinn', 'Europe/Tallinn'), ('America/Sao_Paulo', 'America/Sao_Paulo'), ('Asia/Singapore', 'Asia/Singapore'), ('Africa/Sao_Tome', 'Africa/Sao_Tome'), ('America/Detroit', 'America/Detroit'), ('Europe/Dublin', 'Europe/Dublin'), ('Europe/Tirane', 'Europe/Tirane'), ('Indian/Mahe', 'Indian/Mahe'), ('Asia/Jayapura', 'Asia/Jayapura'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Etc/GMT-14', 'Etc/GMT-14'), ('Asia/Pyongyang', 'Asia/Pyongyang'), ('Factory', 'Factory'), ('Asia/Choibalsan', 'Asia/Choibalsan'), ('Eire', 'Eire'), ('Asia/Magadan', 'Asia/Magadan'), ('Etc/UTC', 'Etc/UTC'), ('America/St_Lucia', 'America/St_Lucia'), ('Australia/West', 'Australia/West'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Europe/Kiev', 'Europe/Kiev'), ('Australia/South', 'Australia/South'), ('Antarctica/Macquarie', 'Antarctica/Macquarie'), ('America/Blanc-Sablon', 'America/Blanc-Sablon'), ('Africa/Johannesburg', 'Africa/Johannesburg'), ('Antarctica/Rothera', 'Antarctica/Rothera'), ('Etc/GMT+9', 'Etc/GMT+9'), ('America/Ojinaga', 'America/Ojinaga'), ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'), ('America/New_York', 'America/New_York'), ('Asia/Hanoi', 'Asia/Hanoi'), ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'), ('Egypt', 'Egypt'), ('Etc/GMT-2', 'Etc/GMT-2'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Asia/Yakutsk', 'Asia/Yakutsk'), ('America/Caracas', 'America/Caracas'), ('GB-Eire', 'GB-Eire'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'), ('America/Hermosillo', 'America/Hermosillo'), ('Africa/Accra', 'Africa/Accra'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Asia/Kathmandu', 'Asia/Kathmandu'), ('EST', 'EST'), ('Asia/Kamchatka', 'Asia/Kamchatka'), ('America/Catamarca', 'America/Catamarca'), ('Africa/Nouakchott', 'Africa/Nouakchott'), ('Asia/Kuwait', 'Asia/Kuwait'), ('Australia/Yancowinna', 'Australia/Yancowinna'), ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'), ('Asia/Baku', 'Asia/Baku'), ('Etc/GMT+3', 'Etc/GMT+3'), ('Asia/Harbin', 'Asia/Harbin'), ('Etc/GMT-5', 'Etc/GMT-5'), ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'), ('America/Puerto_Rico', 'America/Puerto_Rico'), ('Pacific/Rarotonga', 'Pacific/Rarotonga'), ('Europe/Paris', 'Europe/Paris'), ('America/Guadeloupe', 'America/Guadeloupe'), ('Etc/GMT+4', 'Etc/GMT+4'), ('Pacific/Bougainville', 'Pacific/Bougainville'), ('Asia/Oral', 'Asia/Oral'), ('Asia/Katmandu', 'Asia/Katmandu'), ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'), ('Antarctica/Casey', 'Antarctica/Casey'), ('Asia/Qatar', 'Asia/Qatar'), ('Asia/Beirut', 'Asia/Beirut'), ('Europe/Malta', 'Europe/Malta'), ('Pacific/Kwajalein', 'Pacific/Kwajalein'), ('Europe/Budapest', 'Europe/Budapest'), ('Indian/Antananarivo', 'Indian/Antananarivo'), ('Pacific/Enderbury', 'Pacific/Enderbury'), ('Asia/Vladivostok', 'Asia/Vladivostok'), ('Brazil/West', 'Brazil/West'), ('Asia/Hong_Kong', 'Asia/Hong_Kong'), ('Asia/Irkutsk', 'Asia/Irkutsk'), ('America/Adak', 'America/Adak'), ('America/St_Vincent', 'America/St_Vincent'), ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'), ('Indian/Mauritius', 'Indian/Mauritius'), ('GMT0', 'GMT0'), ('Europe/Warsaw', 'Europe/Warsaw'), ('America/Lower_Princes', 'America/Lower_Princes'), ('Asia/Qostanay', 'Asia/Qostanay'), ('America/Los_Angeles', 'America/Los_Angeles'), ('America/Santiago', 'America/Santiago'), ('EET', 'EET'), ('Etc/GMT-3', 'Etc/GMT-3'), ('Africa/Bujumbura', 'Africa/Bujumbura'), ('Asia/Amman', 'Asia/Amman'), ('America/Nome', 'America/Nome'), ('PST8PDT', 'PST8PDT'), ('America/Indiana/Marengo', 'America/Indiana/Marengo'), ('Africa/Algiers', 'Africa/Algiers'), ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'), ('Australia/Queensland', 'Australia/Queensland'), ('Indian/Comoro', 'Indian/Comoro'), ('Libya', 'Libya'), ('America/Belize', 'America/Belize'), ('Etc/GMT-12', 'Etc/GMT-12'), ('Etc/GMT-8', 'Etc/GMT-8'), ('America/Denver', 'America/Denver'), ('Asia/Ashgabat', 'Asia/Ashgabat'), ('Kwajalein', 'Kwajalein'), ('US/Hawaii', 'US/Hawaii'), ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'), ('US/Pacific', 'US/Pacific'), ('Africa/Windhoek', 'Africa/Windhoek'), ('America/Indiana/Knox', 'America/Indiana/Knox'), ('MST7MDT', 'MST7MDT'), ('America/Mazatlan', 'America/Mazatlan'), ('US/Samoa', 'US/Samoa'), ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'), ('America/Yakutat', 'America/Yakutat'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('America/Lima', 'America/Lima'), ('Africa/Mbabane', 'Africa/Mbabane'), ('America/Dawson_Creek', 'America/Dawson_Creek'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Etc/GMT+10', 'Etc/GMT+10'), ('Pacific/Easter', 'Pacific/Easter'), ('America/Curacao', 'America/Curacao'), ('Asia/Pontianak', 'Asia/Pontianak'), ('Africa/Kigali', 'Africa/Kigali'), ('US/Alaska', 'US/Alaska'), ('America/Guatemala', 'America/Guatemala'), ('Asia/Ashkhabad', 'Asia/Ashkhabad'), ('Asia/Dhaka', 'Asia/Dhaka'), ('Australia/North', 'Australia/North'), ('Africa/Bissau', 'Africa/Bissau'), ('America/Fort_Nelson', 'America/Fort_Nelson'), ('America/Metlakatla', 'America/Metlakatla'), ('Antarctica/McMurdo', 'Antarctica/McMurdo'), ('Europe/Tiraspol', 'Europe/Tiraspol'), ('Etc/GMT-9', 'Etc/GMT-9'), ('Pacific/Auckland', 'Pacific/Auckland'), ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'), ('Asia/Dubai', 'Asia/Dubai'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Europe/Bratislava', 'Europe/Bratislava'), ('America/Rosario', 'America/Rosario'), ('Europe/Bucharest', 'Europe/Bucharest'), ('America/Belem', 'America/Belem'), ('Asia/Dili', 'Asia/Dili'), ('America/Fort_Wayne', 'America/Fort_Wayne'), ('America/Halifax', 'America/Halifax'), ('Africa/Banjul', 'Africa/Banjul'), ('Pacific/Guam', 'Pacific/Guam'), ('Africa/Kampala', 'Africa/Kampala'), ('Universal', 'Universal'), ('Europe/Jersey', 'Europe/Jersey'), ('America/Kralendijk', 'America/Kralendijk'), ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'), ('Asia/Thimbu', 'Asia/Thimbu'), ('Pacific/Pohnpei', 'Pacific/Pohnpei'), ('America/Mexico_City', 'America/Mexico_City'), ('Asia/Aqtobe', 'Asia/Aqtobe'), ('Asia/Jakarta', 'Asia/Jakarta'), ('Etc/GMT+7', 'Etc/GMT+7'), ('Africa/Gaborone', 'Africa/Gaborone'), ('Pacific/Wake', 'Pacific/Wake'), ('Asia/Yangon', 'Asia/Yangon'), ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'), ('America/Montserrat', 'America/Montserrat'), ('Asia/Barnaul', 'Asia/Barnaul'), ('Australia/ACT', 'Australia/ACT'), ('Africa/Nairobi', 'Africa/Nairobi'), ('Africa/Abidjan', 'Africa/Abidjan'), ('America/Atikokan', 'America/Atikokan'), ('US/Mountain', 'US/Mountain'), ('Europe/Zurich', 'Europe/Zurich'), ('America/Montevideo', 'America/Montevideo'), ('Etc/GMT+8', 'Etc/GMT+8'), ('Australia/Hobart', 'Australia/Hobart'), ('US/East-Indiana', 'US/East-Indiana'), ('America/Argentina/Salta', 'America/Argentina/Salta'), ('America/Rainy_River', 'America/Rainy_River'), ('Pacific/Tongatapu', 'Pacific/Tongatapu'), ('Asia/Famagusta', 'Asia/Famagusta'), ('Pacific/Tarawa', 'Pacific/Tarawa'), ('CET', 'CET'), ('America/Thule', 'America/Thule'), ('US/Arizona', 'US/Arizona'), ('Europe/Sofia', 'Europe/Sofia'), ('Pacific/Kosrae', 'Pacific/Kosrae'), ('ROK', 'ROK'), ('America/Phoenix', 'America/Phoenix'), ('US/Aleutian', 'US/Aleutian'), ('Asia/Baghdad', 'Asia/Baghdad'), ('Europe/Berlin', 'Europe/Berlin'), ('Turkey', 'Turkey'), ('Etc/GMT+1', 'Etc/GMT+1'), ('Canada/Newfoundland', 'Canada/Newfoundland'), ('Asia/Sakhalin', 'Asia/Sakhalin'), ('Pacific/Midway', 'Pacific/Midway'), ('Australia/LHI', 'Australia/LHI'), ('Etc/GMT-10', 'Etc/GMT-10'), ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'), ('US/Michigan', 'US/Michigan'), ('Australia/Sydney', 'Australia/Sydney'), ('Asia/Seoul', 'Asia/Seoul'), ('Asia/Anadyr', 'Asia/Anadyr'), ('Australia/Darwin', 'Australia/Darwin'), ('America/Ensenada', 'America/Ensenada'), ('America/Cancun', 'America/Cancun'), ('Antarctica/South_Pole', 'Antarctica/South_Pole'), ('Indian/Chagos', 'Indian/Chagos'), ('Atlantic/Stanley', 'Atlantic/Stanley'), ('Europe/Belgrade', 'Europe/Belgrade'), ('America/Santa_Isabel', 'America/Santa_Isabel'), ('Australia/Victoria', 'Australia/Victoria'), ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'), ('Asia/Dushanbe', 'Asia/Dushanbe'), ('Africa/Djibouti', 'Africa/Djibouti'), ('Asia/Nicosia', 'Asia/Nicosia'), ('Pacific/Fakaofo', 'Pacific/Fakaofo'), ('America/Dawson', 'America/Dawson'), ('America/Punta_Arenas', 'America/Punta_Arenas'), ('America/Creston', 'America/Creston'), ('America/Resolute', 'America/Resolute'), ('Asia/Urumqi', 'Asia/Urumqi'), ('America/Chihuahua', 'America/Chihuahua'), ('Africa/Porto-Novo', 'Africa/Porto-Novo'), ('America/Tijuana', 'America/Tijuana'), ('Asia/Brunei', 'Asia/Brunei'), ('Etc/GMT-1', 'Etc/GMT-1'), ('Pacific/Honolulu', 'Pacific/Honolulu'), ('America/Barbados', 'America/Barbados'), ('Pacific/Norfolk', 'Pacific/Norfolk'), ('Australia/Currie', 'Australia/Currie'), ('Antarctica/Troll', 'Antarctica/Troll'), ('Pacific/Wallis', 'Pacific/Wallis'), ('Asia/Chongqing', 'Asia/Chongqing'), ('Indian/Mayotte', 'Indian/Mayotte'), ('GB', 'GB'), ('Canada/Atlantic', 'Canada/Atlantic'), ('Asia/Hebron', 'Asia/Hebron'), ('Asia/Tehran', 'Asia/Tehran'), ('Indian/Maldives', 'Indian/Maldives'), ('Etc/GMT-6', 'Etc/GMT-6'), ('UCT', 'UCT'), ('Atlantic/Bermuda', 'Atlantic/Bermuda'), ('America/Dominica', 'America/Dominica'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Navajo', 'Navajo'), ('America/Thunder_Bay', 'America/Thunder_Bay'), ('GMT-0', 'GMT-0'), ('Asia/Novosibirsk', 'Asia/Novosibirsk'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Portugal', 'Portugal'), ('Africa/Ceuta', 'Africa/Ceuta'), ('America/St_Barthelemy', 'America/St_Barthelemy'), ('America/Edmonton', 'America/Edmonton'), ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'), ('Europe/Madrid', 'Europe/Madrid'), ('Africa/Lusaka', 'Africa/Lusaka'), ('America/Inuvik', 'America/Inuvik'), ('Africa/Juba', 'Africa/Juba'), ('America/Miquelon', 'America/Miquelon'), ('Antarctica/Palmer', 'Antarctica/Palmer'), ('America/Louisville', 'America/Louisville'), ('Japan', 'Japan'), ('Pacific/Chuuk', 'Pacific/Chuuk'), ('Asia/Istanbul', 'Asia/Istanbul'), ('America/Coral_Harbour', 'America/Coral_Harbour'), ('Asia/Khandyga', 'Asia/Khandyga'), ('America/Aruba', 'America/Aruba'), ('Europe/Riga', 'Europe/Riga'), ('America/Havana', 'America/Havana'), ('Africa/Conakry', 'Africa/Conakry'), ('Africa/Lagos', 'Africa/Lagos'), ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'), ('EST5EDT', 'EST5EDT'), ('Africa/Freetown', 'Africa/Freetown'), ('Canada/Pacific', 'Canada/Pacific'), ('Asia/Macau', 'Asia/Macau'), ('America/St_Johns', 'America/St_Johns'), ('Canada/Central', 'Canada/Central'), ('Europe/Zagreb', 'Europe/Zagreb'), ('America/Knox_IN', 'America/Knox_IN'), ('Pacific/Marquesas', 'Pacific/Marquesas'), ('Atlantic/Canary', 'Atlantic/Canary'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('America/Recife', 'America/Recife'), ('America/Juneau', 'America/Juneau'), ('America/Port_of_Spain', 'America/Port_of_Spain'), ('America/Anguilla', 'America/Anguilla'), ('US/Indiana-Starke', 'US/Indiana-Starke'), ('Africa/Blantyre', 'Africa/Blantyre'), ('Africa/Ndjamena', 'Africa/Ndjamena'), ('America/Tortola', 'America/Tortola'), ('Brazil/Acre', 'Brazil/Acre'), ('UTC', 'UTC'), ('Asia/Atyrau', 'Asia/Atyrau'), ('Pacific/Truk', 'Pacific/Truk'), ('Greenwich', 'Greenwich'), ('Pacific/Gambier', 'Pacific/Gambier'), ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'), ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'), ('Etc/GMT', 'Etc/GMT'), ('America/Marigot', 'America/Marigot'), ('America/Grenada', 'America/Grenada'), ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'), ('Europe/London', 'Europe/London'), ('America/Cuiaba', 'America/Cuiaba'), ('Australia/NSW', 'Australia/NSW'), ('America/Indiana/Vevay', 'America/Indiana/Vevay'), ('Antarctica/Syowa', 'Antarctica/Syowa'), ('Asia/Samarkand', 'Asia/Samarkand'), ('Asia/Kolkata', 'Asia/Kolkata'), ('Asia/Jerusalem', 'Asia/Jerusalem'), ('America/Jamaica', 'America/Jamaica'), ('Pacific/Pitcairn', 'Pacific/Pitcairn'), ('America/Scoresbysund', 'America/Scoresbysund'), ('Brazil/DeNoronha', 'Brazil/DeNoronha'), ('Brazil/East', 'Brazil/East'), ('Europe/Rome', 'Europe/Rome'), ('Mexico/BajaSur', 'Mexico/BajaSur'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Antarctica/Mawson', 'Antarctica/Mawson'), ('America/Regina', 'America/Regina'), ('America/Toronto', 'America/Toronto'), ('Europe/Minsk', 'Europe/Minsk'), ('Pacific/Apia', 'Pacific/Apia'), ('Europe/Vienna', 'Europe/Vienna'), ('America/Campo_Grande', 'America/Campo_Grande'), ('Chile/Continental', 'Chile/Continental'), ('Australia/Canberra', 'Australia/Canberra'), ('Africa/Asmera', 'Africa/Asmera'), ('America/Port-au-Prince', 'America/Port-au-Prince'), ('America/Cayenne', 'America/Cayenne'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Asia/Tokyo', 'Asia/Tokyo'), ('Asia/Kuching', 'Asia/Kuching'), ('Asia/Hovd', 'Asia/Hovd'), ('Asia/Bishkek', 'Asia/Bishkek'), ('America/Costa_Rica', 'America/Costa_Rica'), ('Asia/Aqtau', 'Asia/Aqtau'), ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'), ('America/Pangnirtung', 'America/Pangnirtung'), ('Europe/Prague', 'Europe/Prague'), ('Canada/Mountain', 'Canada/Mountain'), ('PRC', 'PRC'), ('Indian/Cocos', 'Indian/Cocos'), ('Atlantic/Azores', 'Atlantic/Azores'), ('Asia/Macao', 'Asia/Macao'), ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'), ('Africa/Khartoum', 'Africa/Khartoum'), ('Africa/Luanda', 'Africa/Luanda'), ('GMT+0', 'GMT+0'), ('America/Monterrey', 'America/Monterrey'), ('Indian/Reunion', 'Indian/Reunion'), ('America/El_Salvador', 'America/El_Salvador'), ('Africa/El_Aaiun', 'Africa/El_Aaiun'), ('Atlantic/Faeroe', 'Atlantic/Faeroe'), ('America/Cordoba', 'America/Cordoba'), ('Pacific/Majuro', 'Pacific/Majuro'), ('Asia/Vientiane', 'Asia/Vientiane'), ('Etc/GMT+11', 'Etc/GMT+11'), ('Europe/Saratov', 'Europe/Saratov'), ('Etc/GMT+2', 'Etc/GMT+2'), ('Africa/Timbuktu', 'Africa/Timbuktu'), ('Europe/Vatican', 'Europe/Vatican'), ('Africa/Asmara', 'Africa/Asmara'), ('America/Indianapolis', 'America/Indianapolis'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'), ('Asia/Dacca', 'Asia/Dacca'), ('Mexico/General', 'Mexico/General'), ('Israel', 'Israel'), ('Africa/Cairo', 'Africa/Cairo'), ('Etc/GMT-7', 'Etc/GMT-7'), ('America/Goose_Bay', 'America/Goose_Bay'), ('Asia/Tashkent', 'Asia/Tashkent'), ('Pacific/Chatham', 'Pacific/Chatham'), ('Iceland', 'Iceland'), ('Australia/Perth', 'Australia/Perth'), ('Zulu', 'Zulu'), ('Asia/Taipei', 'Asia/Taipei'), ('Etc/Universal', 'Etc/Universal'), ('America/Managua', 'America/Managua'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Asia/Kashgar', 'Asia/Kashgar'), ('America/Montreal', 'America/Montreal'), ('Africa/Harare', 'Africa/Harare'), ('America/Godthab', 'America/Godthab'), ('Africa/Ouagadougou', 'Africa/Ouagadougou'), ('America/St_Kitts', 'America/St_Kitts'), ('Mexico/BajaNorte', 'Mexico/BajaNorte'), ('America/Guyana', 'America/Guyana'), ('Pacific/Funafuti', 'Pacific/Funafuti'), ('Europe/San_Marino', 'Europe/San_Marino'), ('America/Rio_Branco', 'America/Rio_Branco'), ('Etc/GMT+6', 'Etc/GMT+6'), ('Africa/Casablanca', 'Africa/Casablanca'), ('America/Antigua', 'America/Antigua'), ('Australia/Melbourne', 'Australia/Melbourne'), ('America/Cambridge_Bay', 'America/Cambridge_Bay'), ('America/Bahia_Banderas', 'America/Bahia_Banderas'), ('Chile/EasterIsland', 'Chile/EasterIsland'), ('Pacific/Galapagos', 'Pacific/Galapagos'), ('Africa/Kinshasa', 'Africa/Kinshasa'), ('Australia/Eucla', 'Australia/Eucla'), ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'), ('Asia/Gaza', 'Asia/Gaza'), ('America/Boise', 'America/Boise'), ('Australia/Lord_Howe', 'Australia/Lord_Howe'), ('Asia/Yerevan', 'Asia/Yerevan'), ('MET', 'MET'), ('America/Nipigon', 'America/Nipigon'), ('Asia/Riyadh', 'Asia/Riyadh'), ('Asia/Tbilisi', 'Asia/Tbilisi'), ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'), ('Africa/Tripoli', 'Africa/Tripoli'), ('America/Sitka', 'America/Sitka'), ('Pacific/Niue', 'Pacific/Niue'), ('Europe/Uzhgorod', 'Europe/Uzhgorod')], default='Europe/Moscow', max_length=50, verbose_name='Часовой пояс'),
        ),
    ]
