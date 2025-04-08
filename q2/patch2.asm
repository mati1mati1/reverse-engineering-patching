jmp 0x50
lea edx, [ebp-0x40C]
mov bl, byte ptr [edx]
mov ecx, 0x804863A
cmp bl, 35
jne not_sh
mov bl, byte ptr [edx+1]
cmp bl, 33
jne not_sh
add edx,2
push edx
mov edx, 0x8048744
call -0x16D
jmp 0x81

not_sh:
    jmp ecx
