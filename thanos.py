�
    <�c�"  �            
       �  � d dl mZ d dlmZ d dlZd dlZd dlmZmZ d dl	m
Z
 d dl mZ d dlmZ d dlmZmZmZmZ d dlmZmZmZmZ d d	lmZ d dlZd d
lmZmZ d dlmZ d dlmZ d dl	Z	d dlZd dlmZmZ d dlZd dlZ e�   �          ej        Zej        Z ej!        Z"ej#        Z$ej%        Z&ej'        Z(e e"e$e&e(gZ)	 d dl*Z*n+# e+$ r#  e,e � de� ��  �          ej-        d�  �         Y nw xY wd� Z.dZ/d� Z0	  e0�   �           e.�   �           e,e dz   ez   �  �          e,e dz   ez   �  �          e,e dz   ez   �  �          e,e dz   ez   �  �          e,e dz   ez   �  �          e,e dz   ez   �  �          e1 e2d�  �        �  �        Z3e3dk    �rog Z4 e5dd�  �        5 Z6 e1 e2de � de"� ��  �        �  �        Z7 e8e7�  �        D ]jZ9 e: e2de � de"� ��  �        �  �        Z;d �<                    e;�=                    �   �         �  �        Z> ej?        e>ge6�  �         e4�@                    e>�  �         �k e,de � d!��  �          e0�   �           e,de � d"��  �         e4D ]mZA ed#eA� �d$d%�  �        ZBeB�C                    eA�  �          e,e � d&��  �          e	j
        d'�  �          eB ee/�  �        �  �         eB�D                    �   �          �n e2d(�  �         ddd�  �         n# 1 swxY w Y   e6�E                    �   �          �n�e3d)k    �r�g ZFg ZG e5dd*�  �        ZH	 	 eF�@                     ejI        eH�  �        �  �         n# eJ$ r Y nw xY w�1eH�E                    �   �           eKeF�  �        d k    r e,e"d+z   �  �          e
d'�  �         �neFD ]�ZL e:eLd          �  �        ZM ed#eM� �d$d%�  �        ZNeN�O                    �   �          eN�P                    �   �         sg	 eN�Q                    eM�  �          e,e � d,eM� d-e� ��  �         �u# e$ r5  e,e" e:eM�  �        z   d.z   ez   �  �         eG�@                    eL�  �         Y ��w xY w�� eKeG�  �        d k    r e,e d/z   �  �          e2d0�  �         �n.eGD ]ZReF�S                    eR�  �         � e5dd1�  �        5 ZTeFD ]Z3e3d          ZU ej?        eUgeT�  �         �	 ddd�  �         n# 1 swxY w Y   eT�E                    �   �           e,e d2z   ez   �  �          e2d0�  �         �n�e3d'k    �rHg ZV e5dd*�  �        ZW	 	 eV�@                     ejI        eW�  �        �  �         n# eJ$ r Y nw xY w�1eW�E                    �   �          d Z9 e,e � d3��  �         eVD ]"ZX e,e � d4e9� d5eXd          � e� ��  �         e9dz  Z9�# e1 e2de � d6e� ��  �        �  �        ZY e:eVeY         d          �  �        ZMeMd7z   ZZej[        d8k    r ej-        d9eZ� ��  �         n ej-        d:eZ� ��  �         eVeY=  e5dd1�  �        ZWeVD ]ZL ej?        eLeW�  �         � e,de � d;e� ��  �          e2d0�  �         eW�E                    �   �          �nOe3d<k    �ro e,de � d=��  �         	  e*j\        d>�  �        Z]n-#   e,e"� d?��  �          e,e"� d@��  �          e^�   �          Y nxY w e_e]j`        �  �        dAk    r� e: e2e � dBe]j`        � dCe"� ��  �        �  �        ZaeadDk    seadEk    seadFk    r� e,e � dG��  �         ej[        d8k    r! ej-        dH�  �          ej-        dI�  �         n  ej-        dJ�  �          ej-        dK�  �          ej-        dL�  �          ej-        dM�  �          e,e � dNe]j`        � ��  �          e2dO�  �          e^�   �          �n e,e � dP��  �          e2dQ�  �         n� e,e � dR��  �          e2dQ�  �         n�e3dSk    r�g ZV e5dd*�  �        ZW	 	 eV�@                     ejI        eW�  �        �  �         n# eJ$ r Y nw xY w�1eW�E                    �   �           e,de&� ��  �          e,dT�  �          e,dU�  �         d Z9eVD ]Zb e,dVebd          � ��  �         e9dz  Z9� e,dU�  �          e2dW�  �         n$e3dXk    r e0�   �           e.�   �           e^�   �          ���)Y�    )�TelegramClient)�PhoneNumberBannedErrorN)�init�Fore)�sleep)�InputPeerChannel)�PeerFloodError�UserPrivacyRestrictedErrorr   �ChatAdminRequiredError)�ChatWriteForbiddenError�UserBannedInChannelError�UserAlreadyParticipantError�FloodWaitError)�InviteToChannelRequest)�ImportChatInviteRequest�AddChatUserRequest)�JoinChannelRequest)�UserStatusRecentlyz#[i] Installing module - requests...zpip install requestsc                  �v   � dd l } d}|D ]/}t           | j        t          �  �        � |� t          � ��  �         �0d S )Nr   u�  
████████╗██╗░░██╗░█████╗░███╗░░██╗░█████╗░░██████╗
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██╔══██╗██╔════╝
░░░██║░░░███████║███████║██╔██╗██║██║░░██║╚█████╗░
░░░██║░░░██╔══██║██╔══██║██║╚████║██║░░██║░╚═══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║╚█████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═════╝░
 )�random�print�choice�colors�n)r   �b�chars      �'/storage/emulated/0/thanosv4/manager.py�bannerr   %   sZ   � ��M�M�M�	�A� � 3� 3������v�&�&�1��1�a�1�1�2�2�2�2�3� 3�    zhttps://t.me/THANOS_PROc                  �z   � t           j        dk    rt          j        d�  �         d S t          j        d�  �         d S )N�nt�cls�clear)�os�name�system� r   r   �clrr(   5   s9   � �	�w�$���
�	�%������
�	�'�����r   Tz[1] Add new accountsz[2] Filter all banned accountsz[3] Delete specific accountsz[4] Update your Scriptz[5] Display All Accountsz[6] Quitz
Enter your choice: �   zvars.txt�ab�
z. [~] Enter How Many Accounts You Want To Add: z+ [~] Enter Phone Number With Country Code: � z# [i] Saved all accounts in vars.txtz" [*] Logging in from new accounts
z	sessions/i��; � 86f861352f0ab76a251866059a6adbd6z[+] Login successful�   z"
 Press enter to goto main menu...�   �rbz4[!] There are no accounts! Please add some and retryz[+] z is not bannedz is banned!zCongrats! No banned accountsz!
Press enter to goto main menu...�wbz[i] All banned accounts removedz [i] Choose an account to delete
�[z] z[+] Enter a choice: z.sessionr!   zdel sessions\zrm sessions/z[+] Account Deleted�   z[i] Checking for updates...zXhttps://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/version.txtz& You are not connected to the internetz) Please connect to the internet and retryg�������?z[~] Update available[Version z]. Download?[y/n]: �y�yes�Yz[i] Downloading updates...z
del add.pyzdel manager.pyz	rm add.pyzrm manager.pyz^curl -l -O https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/add.pyzbcurl -l -O https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/manager.pyz[*] Updated to version: zPress enter to exit...z[!] Update aborted.z Press enter to goto main menu...z5[i] Your Telegram-Members-Adder is already up to date�   z	List Of Phone Numbers Arez:==========================================================�	z
Press enter to goto main menu�   )c�telethon.syncr   �telethon.errors.rpcerrorlistr   �pickler$   �coloramar   r   �timer   �telethon.tl.typesr   r	   r
   r   r   r   r   r   �telethon.tl.functions.channelsr   �sys�telethon.tl.functions.messagesr   r   r   r   r   �RESETr   �LIGHTGREEN_EX�lg�RED�r�WHITE�w�CYAN�cy�YELLOW�yer   �requests�ImportErrorr   r&   r   �THANOSr(   �int�input�a�new_accs�open�g�number_to_add�range�i�str�phone_number�join�split�parsed_number�dump�append�number�c�start�
disconnect�close�accounts�banned_accs�h�load�EOFError�len�account�phone�client�connect�is_user_authorized�send_code_request�m�remove�k�Phone�accs�f�acc�index�session_filer%   �get�version�exit�float�text�prompt�zr'   r   r   �<module>r�      s�  �� (� (� (� (� (� (� ?� ?� ?� ?� ?� ?� � � � � � � � � � � � � � � � � � � � � � � (� (� (� (� (� (� .� .� .� .� .� .� D�  D�  D�  D�  D�  D�  D�  D�  D�  D�  D�  D� H�  H�  H�  H�  H�  H�  H�  H�  H�  H�  H�  H� A� A� A� A� A� A� 
�
�
�
� V� V� V� V� V� V� V� V� =� =� =� =� =� =� 0� 0� 0� 0� 0� 0� ���� ���� � � � � � � � � 	�	�	�	� ���� ������J��	����H���J��	�Y��	�[��
�a��B��	��&��O�O�O�O��� &� &� &�	�E�R�
7�
7�A�
7�
7�8�8�8��B�I�$�%�%�%�%�%�&����3� 3� 3� !��� � �Y��C�E�E�E�
�F�H�H�H�	�E�"�#�
#�A�
%�&�&�&�	�E�"�-�
-�a�
/�0�0�0�	�E�"�+�
+�A�
-�.�.�.�	�E�"�%�
%�a�
'�(�(�(�	�E�"�'�
'��
)�*�*�*�	�E�"�Z�-��/������E�E�)�*�*�+�+�A��A�v�v����T�*�d�#�#� 	:�q��C���&`�2�&`�&`�]^�&`�&`� a� a�b�b�M��U�=�)�)� /� /��"�s�5�5�)`�b�)`�)`�]^�)`�)`�#a�#a�b�b�� "����(:�(:�(<�(<� =� =�����]�O�Q�/�/�/�����.�.�.�.��E�>�r�>�>�>�?�?�?��C�E�E�E��E�>�r�>�>�>�?�?�?�"� � ��"�N�#7�v�#7�#7��Ce�f�f������������1�1�1�2�2�2���
�1������$�$�V�,�,�-�-�-���������E�8�9�9�9�#	:� 	:� 	:� 	:� 	:� 	:� 	:� 	:� 	:� 	:� 	:���� 	:� 	:� 	:� 	:�& 	
���	�	�	�	�	
�a��������D��T�"�"��	��������A���/�/�/�/��� � � �������	�
 	
���	�	�	��3�x�=�=�A����E�!�J�J�K�K�K��E�!�H�H�H�H�#� 4� 4����G�A�J����'��(;�E�(;�(;�W�Gi�j�j����� � � ��0�0�2�2� 4�4��0�0��7�7�7����A�A��A�A�a�A�A�B�B�B�B��1� 4� 4� 4���a���E�
�
�l�]�:�1�<�=�=�=�#�*�*�7�3�3�3�3�3�4����4� �s�;���1�$�$���b�7�7�8�8�8���:�;�;�;�;�$� '� '�A��O�O�A�&�&�&�&��T�*�d�+�+� 0�q�%� 0� 0�� !�!���#���U�G�Q�/�/�/�/�0�0� 0� 0� 0� 0� 0� 0� 0� 0� 0� 0���� 0� 0� 0� 0� ���	�	�	���b�:�:�1�<�=�=�=���:�;�;�;�;�	
�a������D��T�"�"��	�����K�F�K��N�N�+�+�+�+��� � � �������	�
 	
���	�	�	������6�6�6�7�7�7�� 	� 	�C��E�R�*�*�!�*�*�s�1�v�*�q�*�*�+�+�+���F�A�A���E�E�:�r�:�:�q�:�:�;�;�<�<����D��K��N�#�#���z�)���7�d�?�?��B�I�5�|�5�5�6�6�6�6��B�I�3�\�3�3�4�4�4���K��D��T�"�"��� 	$� 	$�G��F�K���#�#�#�#���-�2�-�-�!�-�-�.�.�.���3�4�4�4�	���	�	�	�	�	
�a�����2�2�2�2�2�3�3�3�	�"�h�l�#}�~�~�G�G��	��E�Q�>�>�>�?�?�?��E�Q�A�A�A�B�B�B��D�F�F�F�F�F�����5������$�$��S���"�g�g�7�<�g�g�de�g�g�h�h�i�i�F���}�}��%���6�S�=�=����7�7�7�8�8�8��7�d�?�?��B�I�l�+�+�+��B�I�.�/�/�/�/��B�I�k�*�*�*��B�I�o�.�.�.���	�z�{�{�{���	�~�������C�C�W�\�C�C�D�D�D���.�/�/�/����������0�0�0�1�1�1���8�9�9�9�9��E�R�N�N�N�O�O�O��E�4�5�5�5�5�	
�a������D��T�"�"��	�����K�F�K��N�N�+�+�+�+��� � � �������	�
 	
���	�	�	���i�2�i�i������,�-�-�-���K�L�L�L���� 	� 	�A��E�+�q��t�+�+������F�A�A���K�L�L�L���/�0�0�0�0�	
�a������������������sYs�   �9B> �>%C&�%C&�D4K�K�K�#L3 �3L;�:L;�(O4�47P.�-P.� R/�/R3�6R3�#T' �'T/�.T/�Y# �#(Z�#_+ �+_3�2_3