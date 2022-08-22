#!/usr/bin/python3

from termcolor import colored
import time
import os
import shutil


def banner():
	cols=shutil.get_terminal_size().columns
	os.system('wmctrl -r :ACTIVE: -b add,maximized_vert,maximized_horz')
	print("\n")	
	print(colored("                         -=.                               ................................                                -=.                        ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                       .%@@@.                            +%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+.                            %@@@:                       ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                      :%@@@@:                          =@@@@@@@@@@@@@@@@@@@@@@@@#==========*@@=                          .@@@@@-                      ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                     :@@@@@@:                         +@@@@@@@@@@@@@@@@@@@@@@@*.            .+@+                          @@@@@@=                     ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                    .%@@@@@=                         :@@@@@@@@@@@@@@@@%%@@@@@+                +@-                         :@@@@@@=                    ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                   .%@@@@@-                          #@@###@@##%@@###%  #@@@% .::::            #%                          :@@@@@@-                   ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                   %@@@@@-                          .@@@   @@   @@  .%  #@@@= #@@@@@+          =@:                          .@@@@@@:                  ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                  #@@@@@=                           =@@@   *%   @#  -@%*@@@@. #@@@@@@*...   ..  @=                           .@@@@@@.                 ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                 #@@@@@=                            +@@@=  +*   @-  =#  *@@@  #@@-.@@@=@@= *@@: %+                            .@@@@@%.                ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                =@@@@@=                             +@@@@  =+   +:  @#  *@@@  #@@- @@@ @@# @@@  %+                             :@@@@@*                ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("               :@@@@@+                              +@@@@  .:    .  @#  *@@@  #@@%@@@% %@@:@@#  %+                              -@@@@@=               ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("               @@@@@#               #%*             +@@@@.    +    =@#  *@@@  #@@@@@%  -@@*@@   %+             +%#.              =@@@@@:              ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("              *@@@@@.             .%@@@+            +@@@@-    %    +@#  *@@@  #@@+::    @@@@%   %+            =@@@@.              *@@@@%              ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("             =@@@@@:             .@@@@@#            +@@@@%   .@    %@#  *@@@  #@@-      #@@@=   %+            *@@@@@.              %@@@@*             ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("            .@@@@@=             .@@@@@@:            -@@@@@   -@    @@#  *@@@  #@@-      -@@@   .@-            :@@@@@@:             .@@@@@:            ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("            #@@@@#             .@@@@@@=              @@@@@*++#@*++*@@%++%@@#  -==.      -@@#   +@.             -@@@@@@:             +@@@@%            ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("           .@@@@@              %@@@@@=               *@@@@@@@@@@@@@@@@@@@@@-            #@@:   %#               -@@@@@@.             %@@@@-           ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("           @@@@@=             *@@@@@-        .       .@@@@@@@@@@@@@@@@@@@@#             @@%   %@:                :@@@@@%             -@@@@@           ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("          -@@@@%             +@@@@@-        %@@-      :@@@@@@@@@@@@@@@@@@%.                 :@@:       @@@:       :@@@@@*             *@@@@+          ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("          @@@@@:            =@@@@@=       .%@@@%       .#@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%@@%.       #@@@@-       -@@@@@-            .%@@@@.         ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("         =@@@@*            .%@@@@+       .@@@@@%         :=**#############################*=:         #@@@@@-       +@@@@@.            =@@@@*         ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("         %@@@@.            #@@@@#       .%@@@@@=                                                      .@@@@@@:       #@@@@%             %@@@@:        ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("        -@@@@*            -@@@@@.      .#@@@@@=                                                        :%@@@@@:      .%@@@@=            =@@@@+        ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("        #@@@@.            @@@@@=       *@@@@@=                                                          :@@@@@%.      -@@@@@.            @@@@@.       ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("       :@@@@#            +@@@@*       =@@@@@-      :=:                                          :+-      :@@@@@*       *@@@@#            +@@@@=       ","blue",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("       *@@@@.           :@@@@@.      :@@@@@=      *@@@:              .-+*#@@@@@%+.             -@@@*      :@@@@@=       @@@@@:            @@@@%       ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("       %@@@@            +@@@@=       %@@@@#      #@@@@-            -@@@@@@@@@@@@@@%-           *@@@@%      :@@@@@:      =@@@@#            #@@@@:      ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("      =@@@@-           :@@@@%.      +@@@@@      *@@@@@:          .%@@@@@@@@@@@@@@@@@#.         +@@@@@%      *@@@@#       %@@@@:           :@@@@*      ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("      *@@@@            +@@@@-       @@@@@:     -@@@@@#          .@@@@@@@@@@@@@@@@@@@@%.         *@@@@@+     .@@@@@-      -@@@@*            @@@@%      ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("      %@@@%           .@@@@@.      *@@@@#     :@@@@@#          .@@@@@@@@@@@@@@@@@@@@@@@:         *@@@@@-     -@@@@%       @@@@@.           *@@@@.     ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("     -@@@@=           =@@@@=       @@@@@     .%@@@@#          .%@@@@@@@@@@@@@@@@@@@@@@@@.         #@@@@@.     #@@@@-      -@@@@+           .@@@@+     ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("     *@@@@            #@@@@.      %@@@@=     +@@@@%.          #@@@@@@@@@@@@@@@@@@@@@@@@@#          %@@@@#     :@@@@@       @@@@%            %@@@%     ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("     %@@@%           .@@@@#       @@@@%     -@@@@@.          -@@@+*@@@@@@@@@@@@@@@@@@@@@@-         .@@@@@=     *@@@@.      *@@@@:           #@@@@     ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("     @@@@*           =@@@@.      =@@@@+     *@@@@-           @@@% @@@@@@@@@@@@@@@@@@@@@@@*          -@@@@%     -@@@@+      .@@@@*           =@@@@.    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    :@@@@-           #@@@@       @@@@@     :@@@@@           -@@@.+@@@@@@@@@@@@@@@@@@@@@@@@.          %@@@@+     %@@@@       @@@@#            @@@@+    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    =@@@@.           @@@@#       @@@@#     #@@@@.           *@@@ %@@@@@@@@@@@@@@@@@@@@@@@@-           @@@@%     =@@@@:      *@@@@            %@@@%    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    #@@@@           :@@@@=      -@@@@-    .@@@@%            %@@: @@@@@@@@@@@@@@@@@@@@@@@@@+           *@@@@:    :@@@@+      .@@@@=           #@@@@    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    %@@@#           =@@@@       #@@@@     *@@@@:            @@% +@@@@@@@@@@@@@@@@@@@@@@@@@+            @@@@#     #@@@@       @@@@#           *@@@@    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    @@@@*           #@@@%       @@@@%     @@@@%             @@= @@@@@@@@@@@@@@@@@@@@@@@@@@+            %@@@@     =@@@@.      %@@@%           =@@@@    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    @@@@+           %@@@#      .@@@@+     @@@@*             @@ :@@@@@@@@@@@@@@@@@@@@@@@@@@+            =@@@@:    -@@@@:      *@@@%           :@@@@    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    @@@@=           @@@@*      :@@@@:    :@@@@-             @@ +@@@%+:=#@@@@@@@%=-#@@@@@@@+            .@@@@+    .@@@@=      =@@@@           .@@@@-   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   .@@@@-           @@@@+      =@@@@.    +@@@%              @@ *@@#     *@@@@@.    -@@@@@@=             %@@@%     @@@@*      :@@@@:           @@@@+   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   :@@@@:          .@@@@-      +@@@@     %@@@#              #@.#@@       %@@@:      +@@:@@-             #@@@@     %@@@@      .@@@@-           @@@@*   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   -@@@@.          :@@@@:      *@@@@     @@@@+              +@.#@+       #@@@       :@@ %@:             =@@@@     #@@@@       @@@@=           %@@@#   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   -@@@@.          :@@@@.      *@@@@     @@@@+              :@.#@-       #@@@       .@@ %@              =@@@@.    *@@@@       @@@@+           %@@@%   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   -@@@@.          -@@@@.      #@@@@    .@@@@=               % *@:      .@@@@-       @# %+              -@@@@.    +@@@@       @@@@+           %@@@%   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   -@@@@.          -@@@@.      #@@@@    .@@@@=               . #@:      #@@@@@       %# -               -@@@@.    +@@@@       @@@@*           %@@@%   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   -@@@@.          -@@@@.      *@@@@    .@@@@=                .@@=     *@@- @@#     :@@                 -@@@@.    *@@@@       @@@@+           %@@@%   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   -@@@@:          -@@@@.      *@@@@     @@@@+              .%@@@@:  -@@@*  %@@@.  :@@@#:               -@@@@.    #@@@@       @@@@+           %@@@#   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   :@@@@:          :@@@@:      +@@@@.    @@@@+              -@@@@@@@@@@@@-  +@@@@@@@@@@@@=              =@@@@     %@@@@       @@@@=           @@@@*   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   .@@@@-          .@@@@-      =@@@@.    @@@@*              -@@@@@@@@@@@@.  :@@@@@@@@@@@@=              *@@@@     %@@@*      .@@@@-           @@@@+   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("   .@@@@=           @@@@=      :@@@@:    #@@@%               +@@@@@@@@@@%    @@@@@@@@@@@%               %@@@@    .@@@@=      :@@@@:          .@@@@-   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    @@@@=           @@@@*      .@@@@=    =@@@@.               .#@@@@@@@@*    @@@@@@@@@@#.               @@@@#    -@@@@-      =@@@@.          :@@@@.   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    @@@@*           %@@@#       @@@@%     @@@@+                 .+%@@@@@%#@@%@@@@@@@@+.                -@@@@-    =@@@@.      *@@@%           =@@@@    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    %@@@#           #@@@%       #@@@@     @@@@#                    *@@@@@@@@@@@@@@@+                   #@@@@     #@@@@       %@@@%           *@@@@    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    #@@@@           +@@@@       -@@@@:    #@@@@.                    #@@@@@@@@@@@@@=                    @@@@%    .@@@@+       @@@@#           #@@@@    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    =@@@@.          :@@@@-      .@@@@#    :@@@@#                 =. :@@@@@@@@@@@@*  .                 =@@@@=    =@@@@:       @@@@+           %@@@%    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("    :@@@@-          .@@@@*       @@@@@     @@@@@                 @%  .#@@@@@@@@@=  %@.                @@@@%     #@@@@.      =@@@@.           @@@@+    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("     @@@@*           %@@@@       =@@@@=    =@@@@#                @@+   . ..::.-   *@@.               +@@@@*    -@@@@*       @@@@%           =@@@@.    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("     %@@@%           +@@@@.       @@@@%     %@@@@:               @@%  @*#-%=%.@.  @@%               .@@@@@.    *@@@@.       @@@@*           #@@@@     ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("     *@@@@           :@@@@*       #@@@@=    =@@@@@.              @@@  --*-%-%.*  .@@%               %@@@@+    :@@@@%       =@@@@-           %@@@%     ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("     -@@@@-           %@@@@       .@@@@%     #@@@@*              @@@.       .    =@@#              *@@@@%     #@@@@-       @@@@%           .@@@@+     ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("      %@@@%           +@@@@:       *@@@@*    :@@@@@+             @@@-            *@@*             =@@@@@:    -@@@@%       :@@@@*           *@@@@.     ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("      *@@@@           :@@@@%        @@@@@.    =@@@@@+            %@@* =.+.:. -   @@@+            =@@@@@+     @@@@@-       %@@@@:           @@@@%      ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("      =@@@@-           *@@@@:       =@@@@@     *@@@@@+           -@@@=-*%-%+ @  +@@@.           =@@@@@%     *@@@@#       :@@@@#           :@@@@*      ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("       %@@@@           :@@@@%        %@@@@#     %@@@@@:           *@@@%:. :  ..*@@@*           -@@@@@@     -@@@@@.       #@@@@-           #@@@@:      ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("       *@@@@.           *@@@@-       :@@@@@=     %@@@@-            *@@@@@@@%%@@@@@%            *@@@@@     :@@@@@=       :@@@@%           .@@@@%       ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("       -@@@@#           :@@@@%        =@@@@@-     %@@@-            .@@@@@@@@@@@@@@:            +@@@%     :@@@@@*        %@@@@-           =@@@@=       ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("        %@@@@.           #@@@@+        #@@@@@-    .*@*              -@@@@@@@@@@@@:              +@*.    .%@@@@@.       =@@@@@            @@@@@.       ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("        =@@@@*           .@@@@@:       .%@@@@@-                      -@@@@@@@@@%:                      .%@@@@@:       .@@@@@.           -@@@@*        ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("         @@@@@.           +@@@@%        .@@@@@@-                       .:--:::.                       .@@@@@@-        #@@@@#            %@@@@:        ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("         =@@@@*            %@@@@*        .@@@@@%                                                      #@@@@@-        *@@@@@            =@@@@#         ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("          @@@@@:           :@@@@@:        .@@@@%                                                      #@@@@+        -@@@@@-           .%@@@@.         ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("          =@@@@#            *@@@@@.        .@@@+                                                      .@@@=        .@@@@@*            +@@@@*          ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("           @@@@@-            #@@@@@.         ..                                                         :         .@@@@@%            :@@@@@.          ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("           :@@@@@            .%@@@@@.                                                                            .%@@@@@.            #@@@@=           ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("            #@@@@#            :@@@@@%.                                                                          .#@@@@@:            =@@@@%            ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("            .@@@@@=            -@@@@@%:                                                                        :%@@@@@-            .@@@@@-            ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("             =@@@@@:            =@@@@@%.                                                                      .%@@@@@=             %@@@@*             ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("              #@@@@%             =@@@@@#                                                                      +@@@@@=             *@@@@%.             ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("              .@@@@@*             -@@@@*                                                                      +@@@@=             =@@@@@-              ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("               :@@@@@+             :@@%                                                                        %@@-             -@@@@@=               ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                =@@@@@=              .                                                                          .              :@@@@@*                ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                 #@@@@@=                                                                                                      :@@@@@%.                ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                 .%@@@@@-                                                                                                    .%@@@@@.                 ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                  .%@@@@@-                                                                                                  .%@@@@@:                  ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                   .@@@@@@-                                                                                                .@@@@@@-                   ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                    .@@@@@@-                                                                                              :@@@@@@=                    ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                     :@@@@@@:                                                                                             @@@@@@=                     ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                      :@@@@@:                                                                                            .@@@@@-                      ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                       .@@@@.                                                                                             @@@@:                       ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print(colored("                         **.                                                                                              .**.                        ","red",attrs=['blink']).center(cols))
	time.sleep(0.038)
	print("\n\n")	
	print(("                                                                                                                                                                                                     "+colored("{0x48616D6D6552}","cyan",attrs=['underline'])).center(cols))                                                                                                                                                   
	print("\n\n\n")
