from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.yatim(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`šš¢š”š” ššššØš­ šš® ššš­š¢š¦ !`")
    sleep(2)
    await typew.edit("`šš¦šš¤ , ššš©šš¤.. ššØš¤ šš¢ ššš§šš¦ !`")
    sleep(1)
    await typew.edit("`šš¢ ššš§šš¦ ššš¤ šš¢š§š š¤šØš§š  , šššššššššš`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\nā»ā³|ā-ā©`"
                     "`\nā³ā»|     ć½`"
                     "`\nā»ā³|    ā |`"
                     "`\nā³ā»|ā¼) _ć`"
                     "`\nā»ā³|ļæ£  )`"
                     "`\nā³ļ¾(ļæ£ ļ¼`"
                     "`\nā»ā³Tļæ£|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.bagas(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**IZINKAN SAYA INTRO**")
    sleep(1)
    await typew.edit("**GW ATHEIS**")
    sleep(1)
    await typew.edit("**SOLOYOLOO**")
    sleep(1)
    await typew.edit("**WAZZUP MY FRIENDS**")
    sleep(1)
    await typew.edit("**SOBAT SEKON GUA**")
    sleep(1)
    await typew.edit("**FAKKLAH..**")
    sleep(1)
    await typew.edit("**NGENSKUYY..**")
    sleep(1)
    await typew.edit("**ANJASS BROHHH..**")
    sleep(1)
    await typew.edit("**KENALIN GUA BAGAS**")
    sleep(1)
    await typew.edit("**BACOTNYA KADANG NGEGAS**")
    sleep(1)
    await typew.edit("**TAPI JANGAN BAPER**")
    sleep(1)
    await typew.edit("**GW IMIGRAN DARI SURGA YANG DITURUNKAN KE BUMI**")
    sleep(2)
    await typew.edit("**DI MALAM PENGANTIN DAN TEGANG**")
    sleep(1)
    await typew.edit("**AYAH GUA GA BEKERJA SENDIRIAN, DIA DI BANTU IBU GUA**")
    sleep(2)
    await typew.edit("**IBU GUA TUGASNYA**")
    sleep(1)
    await typew.edit("**MENYIMPAN HASIL SELUNDUPAN**")
    sleep(1)
    await typew.edit("**GUA ANAK KE DUA DARI TIGA BERSAUDARA**")
    sleep(2)
    await typew.edit("**UMUR GW 20 DI TAMBAH 3 DI KURANGIN 1**")
    sleep(2)
    await typew.edit("**ASKOT GUA JATENG**")
    sleep(1)
    await typew.edit("**PAS NYA DI SOLO**")
    sleep(1)
    await typew.edit("**NTAR KALO MAU MAIN PC AJA, TAPI BAWA ROKOK AMA KOPI JANGAN NYUSAHIN GW SUU**")
    sleep(3)

@register(outgoing=True, pattern='^.lah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lo tolol?`")
    sleep(1)
    await typew.edit("`Apa dongok?`")
    sleep(1)
    await typew.edit("`Gausah sok keras`")
    sleep(1)
    await typew.edit("`Gua ga ketrigger sama bocah baru nyemplung!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut š¤”`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badutš¤”, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")
    
@register(outgoing=True, pattern='^.gc(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`SUPPORT.. `")
    sleep(1)
    await typew.edit("`CENGHA...`")
    sleep(1)
    await typew.edit("`SUCCESSFULLY COMPELED`")
    sleep(1)
    await typew.edit("`šSUPPORT` @allfucek š CENGHA` @loveisfuckedup")



CMD_HELP.update({
    "bagasbot":
    "`.bagas`\
    \nUsage: menampilkan alive bot.\
    \n\n`.yatim`\
    \n\n`.lah`\
    \nUsage: hiks\
    \n\n`.gc`\
    \nUsage: support\
    \n\n`.punten` ; `.sayonara`\
    \nUsage: misi."
    
})
