#! /bin/bash

lyrics_string="Quisiera:Ayer:cambiarle:conocí:el:un:final
:cielo:al:sin:cuento|Las:sol|Y:barras:un:y:hombre:los:sin
:tragos:suelo|Un:han:santo:sido:en:testigo|De:prision|Y:el
:una:dolor:canción:que:triste:me:sin:causaste:dueño|Y:y
:conocí:to':tus:lo:ojos:que:negros|Y:hciste:ahora:conmigo|Un
:sí:infeliz:que:en:no:el:puedo:amor,:vivir:que:sin:aun
:ellos:no:yo|Le:te:pido:supera|Que:al:ahora:cielo:camina
:solo:solo:un:sin:deseo|Que:nadie:en:por:tus:todas:ojos
:las:yo:aceras|Preguntándole:pueda:a:vivir|He:Dios:recorrido
:si:el:en:mundo:verad:entero|te:el:vengo:amor:a:existe|:decir|"

echo " "
#put all of the lyrics into a new array
both_songs=$(echo $lyrics_string | sed 's/|/\\n/g')
declare -a songs=()
#serparate them by :
songs=($(echo "$both_songs" | tr ':' '\n'))

#add every other lyric to the respective songs
i=0
declare -a song1=()
declare -a song2=()
while [ $i -lt ${#songs[*]} ];
do
	song1+=(${songs[$i]})
	song2+=(${songs[$i+1]})
	i=$(($i+2))
done

#print the songs
echo -e ${song1[*]}
echo " "
echo -e ${song2[*]}
#remove new lines and upper case letters
i=0
while [ $i -lt ${#song1[*]} ];
do
	song1[$i]=$(echo ${song1[$i]} | tr [:upper:] [:lower:])
	song1[$i]=$(echo ${song1[$i]} | sed 's/\\n/ /g')
	i=$(($i+1))
done
i=0
while [ $i -lt ${#song2[*]} ];
do
	song2[$i]=$(echo ${song2[$i]} | tr [:upper:] [:lower:])
	song2[$i]=$(echo ${song2[$i]} | sed 's/\\n/ /g')
	i=$(($i+1))
done

#check to see if the songs have the same lyrics, then add them to a new array, sort
#them and print them
declare -a both=()
for i in ${song1[*]};
do
	for j in ${song2[*]};
	do
		if [ $i == $j ];then
			flag="f"
			for k in ${both[*]};
			do
				if [ $i == $k ];then
					flag="t"
				fi
			done
			if [ $flag == "f" ];then
				both+=($i)
			fi
		fi
	done
done


both=($(for i in ${both[*]}; do echo $i; done | sort -n))

echo "Words that are in both songs: ${both[*]}"
echo " "
read -p "Press enter to exit the script"
