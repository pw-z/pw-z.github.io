#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *fp;
	if (fp = fopen("stu.dat","r") == NULL)
		fp = fopen ("stu.dat","w");
    fclose(fp);
    system("menu.exe");
    return 0;
}
