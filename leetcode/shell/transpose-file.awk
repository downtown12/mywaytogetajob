{for(j=1;j<=NF;j++) row[NR][j] = $j;}

END{
		for(j=1;j<=NF;j++){
			for(i=1;i<=NR;i++){
					if(i<NR){printf "%s ",row[i][j]}
					else{printf "%s\n",row[i][j]}
			}
		}
}
