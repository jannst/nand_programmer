cmake_minimum_required(VERSION 3.13)
include(pico_sdk_import.cmake)
project(firmware_pico C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
pico_sdk_init()

add_executable(firmware_pico
    src/main.c
)

pico_enable_stdio_usb(firmware_pico 1)
pico_enable_stdio_uart(firmware_pico 1)
pico_add_extra_outputs(firmware_pico)
target_link_libraries(firmware_pico pico_stdlib)