ó
3]c           @   s   d  d l  Z  d  d l Td  d l m Z d  d l Z d  d l Z d Z d Z d Z d Z	 d   Z
 d   Z d	   Z e d
 k r e
   e   n  d S(   iÿÿÿÿN(   t   *(   t   systems   [91ms   [0ms   [41mc           C   s?   t  j d  t d t GHt d t d t d t d GHd  S(   Nt   clears.  @@@  @@@  @@@  @@@@@@@@   @@@@@@    @@@@@@@@   @@@@@@ 
@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@  @@@@@@@@ 
@@!  @@!@!@@@  @@!       @@!  @@@  !@@        @@!  @@@ 
!@!  !@!!@!@!  !@!       !@!  @!@  !@!        !@!  @!@ 
!!@  @!@ !!@!  @!!!:!    @!@  !@!  !@! @!@!@  @!@!@!@! 
!!!  !@!  !!!  !!!!!:    !@!  !!!  !!! !!@!!  !!!@!!!! 
!!:  !!:  !!!  !!:       !!:  !!!  :!!   !!:  !!:  !!! 
:!:  :!:  !:!  :!:       :!:  !:!  :!:   !::  :!:  !:! 
 ::   ::   ::   ::       ::::: ::   ::: ::::  ::   ::: 
:    ::    :    :         : :  :    :: :: :    :   : :
s    Author : Mr.KaitoX s    V1.0 s    Information Gathering s   
(   t   osR   t   Rt   Nt   BGRt   BGN(    (    (    s   infogathering.pyt   banner   s    c           C   sÄ  d t  d t d GHd t  d t d GHd t  d t d GHd t  d t d	 GHd t  d
 t d GHd t  d t d GHd t  d t d GHd t  d t d GHd t  d t d GHd t  d t d GHd t  d t d GHd t  d t d GHd t  d t d GHd t  d t d GHd t  d t d GHd t  d  t d! GHd t  d" t d# GHd t  d$ t d% GHd t  d& t d' GHd t  d( t d) GHd t  d* t d+ GHt   d  S(,   Nt   [t   01s   ] Traceroutet   02s   ] Test Pingt   03s   ] DNS lookupt   04s   ] Reverse DNSt   05s   ] Host Recordt   06s   ] Subdomain Findert   07s   ] Find DNS servert   08s   ] Zone transfert   09s   ] Whois Lookupt   10s   ] Geo IP Lookupt   11s   ] Reverse IP Lookupt   12s   ] TCP Port Scant   13s   ] Subnet Lookupt   14s   ] ASN Lookupt   15s   ] HTTP Headert   16s   ] Extract Page Linkt   17s   ] Reverse Analytics Searcht   18s   ] IP Scannert   19s   ] Web IP Findert   20s   ] Aboutt   00s   ] EXIT(   R   R   t   root(    (    (    s   infogathering.pyt   menu   s,    c    '      C   s  t  d  }  |  d k s$ |  d k r[ t  d  } d | } t |  j   } | GHt   n!|  d k ss |  d k rª t  d  } d | } t |  j   } | GHt   nÒ|  d	 k sÂ |  d
 k rù t  d  } d | } t |  j   } | GHt   n|  d k s|  d k rHt  d  } d | } t |  j   }	 |	 GHt   n4|  d k s`|  d k rt  d  } d | }
 t |
  j   } | GHt   nå|  d k s¯|  d k rt  d  } t j d |  } t j | j  } d | GHx| d D] } | GHqôWnv|  d k s|  d k rUt  d  } d | } t |  j   } | GHt   n'|  d k sm|  d k r¤t  d  } d | } t |  j   } | GHt   nØ|  d  k s¼|  d! k rót  d"  } d# | } t |  j   } | GHt   n|  d$ k r6t  d%  } d& | } t |  j   } | GHt   nF|  d' k ryt  d%  } d( | } t |  j   } | GHt   n|  d) k r¼t  d*  } d+ | } t |  j   } | GHt   nÀ|  d, k rÿt  d-  } d. | } t |  j   } | GHt   n}|  d/ k rBt  d%  } d0 | } t |  j   } | GHt   n:|  d1 k rt  d2  } d3 | } t |  j   }  |  GHt   n÷|  d4 k rÈt  d2  } d5 | }! t |!  j   }" |" GHt   n´|  d6 k rt  d  } d7 | }# t |#  j   }$ |$ GHt   nq|  d8 k rvt  d9  }% t j d: |%  } t j | j  } | d; } x'| D] } | d< GHt   qYWn|  d= k rát  d  } t j d |  } t j | j  } | d; }& x¼ |& D] } | d> GHt   qÄWn |  d? k rüd@ GHt   n |  dA k s|  dB k r#dC GHt	   nY |  dD k rFt
 dE t GHt   n6 |  dF k s^|  dG k r|t j dH  t   t   n  d  S(I   Ns   RootSec:~# R
   t   1s   [0mEnter IP or Domain: s$   https://api.hackertarget.com/mtr/?q=R   t   2s&   https://api.hackertarget.com/nping/?q=R   t   3s   [0mEnter Domain: s*   https://api.hackertarget.com/dnslookup/?q=R   t   4s&   [0mEnter Domain/Ip Address/IP Range: s+   https://api.hackertarget.com/reversedns/?q=R   t   5s+   https://api.hackertarget.com/hostsearch/?q=R   t   6s?   https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=s   Result subdomain: t
   subdomainsR   t   7s   [0mEnter Server Name: s.   https://api.hackertarget.com/findshareddns/?q=R   t   8s-   https://api.hackertarget.com/zonetransfer/?q=R   t   9s   [0mEnter Ip/Domain: s&   https://api.hackertarget.com/whois/?q=R   s   [0mEnter IP Address: s&   https://api.hackertarget.com/geoip/?q=R   s0   https://api.hackertarget.com/reverseiplookup/?q=R   s   [0mEnter IP address: s%   https://api.hackertarget.com/nmap/?q=R   s    [0mEnter cidr/IP with Netmask: s+   https://api.hackertarget.com/subnetcalc/?q=R   s)   https://api.hackertarget.com/aslookup/?q=R   s   [0mEnter Web Address: s,   https://api.hackertarget.com/httpheaders/?q=R   s*   https://api.hackertarget.com/pagelinks/?q=R   s0   https://api.hackertarget.com/analyticslookup/?q=R   s   [0mEnter IP: s7   https://www.threatcrowd.org/searchApi/v2/ip/report/?ip=t   resolutionst   domainR   t
   ip_addressR   s¢   [0m[[91m*[0m] Name: Information Gathering 
[[91m~[0m] Author : Mr.KaitoX  
[[91m~[0m] Youtube : YOUTUBE.COM/KAITOLEGION 
[[91m+[0m] Team  : Pinoy RootSecR   t   0s
   Bye Bye :)t    s   [+] Select Numbert   helpt   HELPR   (   t	   raw_inputt   urlopent   readR   t   requestst   gett   jsont   loadst   textt   exitR   R   R   R   R   R    ('   t   rootsect   juniort   tracet   routet   testt   pingt   dnst   lookt   revt   verst   hostt   rect   masukant   resultt   jt   it   aaat   abt   zont   trant   wht   iost   geot   ipt   akt   tct   prtt   subt   nett   asnt   lopt   httpt   headt   extrt   paget   anat   labt   pilt   kld(    (    s   infogathering.pyR   ,   s
   









	






















	
	


t   __main__(   t   syst   urllib2t   platformR   R5   R7   R   R   R   R   R   R    R   t   __name__(    (    (    s   infogathering.pyt   <module>   s   
			¢


	Developer : Mr.KaitoX