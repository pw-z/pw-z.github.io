#include <stdio.h>
#include <string.h>

struct grade
{
    int number;
    char name[60];
    int math;
    int phy;
    int eng;
    int total;
}student[100];

int main()
{
    FILE *fp = fopen("stu.dat","r");
    int i ,j;
    for(i=0;!feof(fp);i++)
    {
        fscanf(fp,"%d  %s  %d  %d  %d  %d",&student[i].number,student[i].name,&student[i].math,&student[i].phy,&student[i].eng,&student[i].total);
    }
    fclose(fp);
    struct grade change;
	printf("您即将更改一个同学的成绩信息，请输入此同学的学号:");
	scanf("%d",&change.number);  
    int I = 0,J = 0;
    for (;I < i;I ++)
    {
            if (student[I].number == change.number)
            {
            	strcpy(change.name,student[I].name); 
				printf("%s同学目前的成绩为：\n数学:%d物理:%d英语:%d总分:%d\n",change.name,student[I].math,student[I].phy,student[I].eng,student[I].total); 
				printf("请输入此同学的修正成绩（格式：数学 物理 英语 总分）:");
				scanf("%d %d %d %d",&change.math,&change.phy,&change.eng,&change.total);
            	student[I] = change;
            	printf("%s成绩修改成功，按任意键返回主菜单。",student[I].name);
            }    	
    }
    fopen("stu.dat","wb");
    for(j=0;j<i;j++)
    {
        fprintf(fp,"\n%d  %s  %d  %d  %d  %d",student[j].number,student[j].name,student[j].math,student[j].phy,student[j].eng,student[j].total);
    }
    fclose(fp);
    system("pause");
    return 0;
}


















