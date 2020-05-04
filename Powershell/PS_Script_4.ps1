clear

$song=("Quisiera:Ayer:cambiarle:conocí:el:un:final" + ":cielo:al:sin:cuento|Las:sol|Y:barras:un:y" + ":hombre:los:sin:tragos:suelo|Un:han:santo:" +               "sido:en:testigo|De:prision|Y:el:una:dolor:" + "canción:que:triste:me:sin:causaste:dueño|Y:" + "y:conocí:to':tus:lo:ojos:que:negros|Y:hiciste" +               ":ahora:conmigo|Un:sí:infeliz:que:en:no:el:" + "puedo:amor,:vivir:que:sin:aun:ellos:no:yo|" +  "Le:te:pido:supera|Que:al:ahora:cielo:camina" +               ":solo:solo:un:sin:deseo|Que:nadie:en:por:tus" + ":todas:ojos:las:yo:aceras|Preguntándole:pueda" + ":a:vivir|He:Dios:recorrido:si:el:en:mundo:verdad" + ":entero|te:el:vengo:amor:a:existe|:decir|") 

#initialize arrays
$song1 = @()
$song2 = @()

#store lyrics into string
$lyrics_array = @()
$lyrics_array += $song.Replace('|', "`r`n").Split(':')

#add each lyric to its correct song
for ($i = 0; $i -lt $lyrics_array.Length; $i+=2)
{
    $song1 += $lyrics_array[$i]
    $song2 += $lyrics_array[$i+1]
}

#print songs
Write-Host $song1
Write-Host $song2

#store individual words into new arrays to remove "`n"
$song11 = @()
$song22 = @()
foreach ($i in $song1)
{
    if ($i.Contains("`n"))
    {
        $song11 += $i.Split("`n")
    }
    else
    {
        $song11 += $i
    }
} 

foreach ($i in $song2)
{
    if ($i.Contains("`n"))
    {
        $song22 += $i.Split("`n")
    }
    else
    {
        $song22 += $i
    }
} 

#check every lyric to see if it is in the other song
#add it to $both if it is
$both = @()
foreach ($i in $song11)
{
    $new_i = $i.ToLower().trim(" ")
    $new_i = $new_i.trim("`n")
    foreach ($j in $song22)
    {

        $new_j = $j.ToLower().trim(" ")
        $new_j = $new_j.trim("`n")
        #Write-Host $new_i
        #Write-host $new_j
        #Write-Host
        if ($new_i -eq $new_j)
        {
            #check to make sure it has not already been found
            if (-not ($both.Contains($new_i)))
            {
                $both += $new_i
            }
        }

    }
}

$both = $both | sort
Write-Host "Words contained in both songs: `n`n$both`n"

Read-Host -Prompt "Press any key to exit"
