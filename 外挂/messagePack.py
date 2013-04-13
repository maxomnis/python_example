#!/usr/bin/python
# -*- coding:gb2312 -*-
#=======================================================
#@author:jeffxun
#@date  : 2012/12/12
#@context: 压缩消息
#=======================================================
import traceback

# 自身服务器接口
MSG_ON_USER_LOGIN                               =   1
MSG_ON_GENERAL_INFO                             =   5
MSG_ON_GET_TASK                                 =   8
MSG_ON_ONLINE_AWARD                             =   10
MSG_ON_AUTO_FISH                                =   11
MSG_ON_GENERAL_RACE                             =   12
MSG_ON_BATTLE_INFO                              =   13
MSG_ON_GLOBAL_MAP_WAR                           =   20
MSG_ON_NEW_GLOBAL_MAP_WAR                       =   21
MSG_ON_FIGHT_WAR                                =   25
MSG_ON_HEART_LINK                               =   1024

#游戏接口
MSG_ON_SG_USER_LOGIN                            =   1
MSG_ON_SG_GENERAL_INFO                          =   31
#----------------------------------------------
MSG_ON_HX_ADD_GENERAL_BOOLD                     =   43
MSG_ON_HX_ADD_GOLD_BOOLD                        =   46
MSG_ON_HX_SKILL_PET_CARD						=	52
MSG_ON_SG_ROB                                   =   60
#----------------------------------------------
MSG_ON_SG_TASK_INFO                             =   80
MSG_ON_SG_NEWER_TASK                            =   81
MSG_ON_SG_WAR_TASK                              =   83
MSG_ON_SG_REPUTE_TASK                           =   480
MSG_ON_SG_GENERAL_RACE                          =   96
MSG_ON_SG_OPEN_BOX                              =   105
MSG_ON_SG_ROB_COUNT                             =   106
#----------------------钓鱼----------------------------------
MSG_ON_SG_FISH_START                            =   170
MSG_ON_SG_FISH_END                              =   171
MSG_ON_SG_ADD_FISH_START                        =   172
MSG_ON_SG_ADD_FISH_END                          =   173
#---------------------------------------------------------
MSG_ON_SG_REFRESH_SKILL                         =   261
MSG_ON_SG_GENERAL_SKILL							=	264
MSG_ON_SG_AWARD_INFO                            =   289
MSG_ON_SG_ENCOURAGE_AWARD                       =   290
MSG_ON_HX_AWARD_INFO                            =   289
MSG_ON_HX_ENCOURAGE_AWARD                       =   290
MSG_ON_SG_GENERAL_PET							=	343
#-------------------火线对战-------------------------------------
MSG_ON_HX_FIGHT_JOIN                            =   183
MSG_ON_HX_FIGHT_OTHER_JOIN                      =   184
MSG_ON_HX_FIGHT_LEAVE                           =   185
MSG_ON_HX_FIGHT_OTHER_LEAVE                     =   186
MSG_ON_HX_FIGHT_ATTACK                          =   198
MSG_ON_HX_FIGHT_ROOM_PLAYER                     =   416
MSG_ON_HX_FIGHT_INVITE_RONDOM                   =   418
MSG_ON_HX_FIGHT_HAVE_ATTACK                     =   407
#-------------------军团----------------------------------
MSG_ON_SG_BATTLEFIELD                           =   348
MSG_ON_SG_BATTLEFIELD_START                     =   351
MSG_ON_SG_BATTLEFIELD_ATTACK                    =   352
MSG_ON_SG_BATTLEFILED_ATTACKED                  =   354
MSG_ON_SG_BATTLEFIELDEND                        =   355
MSG_ON_SG_BATTLEFIELDBROCK                      =   357
#-------------------比武----------------------------------
MSG_ON_SG_BATTLERACE                            =   376
MSG_ON_SG_BATTLERACEEND                         =   381
MSG_ON_SG_BATTLERACEBROCK                       =   383
#------------------火线旧地图战斗----------------------------
MSG_ON_HX_GLOBALMAP_ROOM_JOIN                   =   401
MSG_ON_HX_GLOBALMAP_ATTACK_NPC                  =   402
MSG_ON_HX_GLOBALMAP_HAVE_ATTACK                 =   404
MSG_ON_HX_GLOBALMAP_ROOM_LEAVE                  =   405
MSG_ON_HX_GLOBALMAP_ROOM_END                    =   406
#------------------火线新地图战斗----------------------------
MSG_ON_HX_NEW_GLOBAL_WAR_TEAM_JOIN              =   394
MSG_ON_HX_NEW_GLOBAL_WAR_TEAM_START             =   401
MSG_ON_HX_NEW_GLOBAL_WAR_TEAM_OTHER_LEAVE       =   399
MSG_ON_HX_NEW_GLOBAL_WAR_TEAM_OTHER_JOIN        =   398
MSG_ON_HX_NEW_GLOBAL_WAR_END                    =   406
MSG_ON_HX_NEW_GLOBAL_WAR_SINGLE_START           =   395 
MSG_ON_HX_NEW_GLOBAL_WAR_SINGLE_ATTACK          =   402
MSG_ON_HX_NEW_GLOBAL_WAR_SINGLE_ATTACKED        =   404
MSG_ON_HX_NEW_GLOBAL_WAR_AUTO_ATTACK            =   473
#----------------------------------------------
MSG_ON_SG_CROSS_BATTLERACE                      =   502
MSG_ON_SG_HEART_LINK                            =   1024

from messageBase import PackBase


class com_sc_UserLogin(PackBase):
    """ """
    def __init__(self):
        PackBase.__init__(self,MSG_ON_USER_LOGIN);
        self.res    =   -1
        self.username    =   ""
        self.nickname    =   ""
    def data(self):
        self.buf.writeShort(self.res)
        self.buf.writeShort(self.strLen(self.username))
        self.buf.writeUTFBytes(self.username)
        self.buf.writeShort(self.strLen(self.nickname))
        self.buf.writeUTFBytes(self.nickname)
        return self.pack()
        
class com_sc_GeneralInfo(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_GENERAL_INFO)
        self.cid    =   0
        self.gids   =   []
        
    def data(self):
        """ """
        self.buf.writeInt(self.cid)
        self.buf.writeShort(len(self.gids))
        for gen in self.gids:
            self.buf.writeShort(self.strLen(gen["gname"]))
            self.buf.writeUTFBytes(gen["gname"])
            self.buf.writeInt(gen["gid"])
        return self.pack()
        
class com_sc_GetTask(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_GENERAL_INFO)
        self.num    = 0
    
    def data(self):
        """ """
        self.buf.writeShort(self.num)
        return self.pack()
        
class com_sc_GlobalMapWar(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_GLOBAL_MAP_WAR)
        self.res    = 0
        
    def data(self):
        """ """
        self.buf.writeShort(self.res)
        return self.pack()

class com_sc_NewGlobalMapWar(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_NEW_GLOBAL_MAP_WAR)
        self.res    = 0
        
    def data(self):
        """ """
        self.buf.writeShort(self.res)
        return self.pack()
        
class com_sc_onLineAward(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_ONLINE_AWARD)
        self.res    = 0
    
    def data(self):
        """ """
        self.buf.writeShort(self.res)
        return self.pack()
        
class com_sc_AutoFish(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_AUTO_FISH)
        self.res    =   0
        
    def data(self):
        """ """
        self.buf.writeShort(self.res)
        return self.pack()

class com_sc_GeneralRace(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_GENERAL_RACE)
        self.res    = 0
        
    def data(self):
        """ """
        self.buf.writeShort(self.res)
        return self.pack()
        
class com_sc_BattleInfo(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_BATTLE_INFO)
        self.res    =   0
    def data(self):
        """ """
        self.buf.writeShort(self.res)
        return self.pack()

class com_sc_onFightWar(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_FIGHT_WAR)
        self.res = 0
    def data(self):
        """ """
        self.buf.writeShort(self.res)
        return self.pack()
        
class com_sg_cs_HeartLink(PackBase):
    """"""
    def __init__(self):
        PackBase.__init__(self,MSG_ON_SG_HEART_LINK)
    
    def data(self):
        return self.pack();
        
class com_sg_cs_userLogin(PackBase):
    """ """
    def __init__(self):
        """"""
        PackBase.__init__(self,MSG_ON_SG_USER_LOGIN);
        self.username   =   ""
        self.password   =   ""
        
    def data(self):
        """"""
        self.buf.writeShort(self.strLen(self.username))
        self.buf.writeUTFBytes(self.username)
        self.buf.writeShort(self.strLen(self.password))
        self.buf.writeUTFBytes(self.password)
        return self.pack()

class com_sg_cs_TaskInfo(PackBase):
    """"""
    def __init__(self):
        """"""
        PackBase.__init__(self,MSG_ON_SG_TASK_INFO);
        self.uid            =   -1
        self.task_type      =   -1
    
    def data(self):
        """"""
        self.buf.writeInt(self.uid)
        self.buf.writeShort(self.task_type);
        return self.pack()
        
class com_sg_cs_NewerTask(PackBase):
    """"""
    def __init__(self):
        """"""
        PackBase.__init__(self,MSG_ON_SG_NEWER_TASK);
        self.uid        =   -1
        self.cid        =   -1
        self.taskid     =   -1
    
    def data(self):
        """"""
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        self.buf.writeShort(self.taskid)
        return self.pack()
        
class com_sg_cs_WarTask(PackBase):
    """"""
    def __init__(self):
        """"""
        PackBase.__init__(self,MSG_ON_SG_WAR_TASK);
        self.uid    =   -1
        self.cid    =   -1
        self.taskid =   -1
    
    def data(self):
        """"""
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        self.buf.writeShort(self.taskid)
        return self.pack()

class com_sg_cs_ReputeTask(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_REPUTE_TASK);
        self.uid    =   -1
        self.cid    =   -1
        self.taskid =   -1
    def data(self):
        """"""
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        self.buf.writeShort(self.taskid)
        return self.pack()
        
class com_sg_cs_GeneralInfo(PackBase):
    """"""
    def __init__(self):
        PackBase.__init__(self,MSG_ON_SG_GENERAL_INFO);
        self.uid    =   -1
        self.cid    =   -1
    
    def data(self):
        """"""
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        return self.pack();
        
class com_hx_cs_GeneralInfo(PackBase):
    """"""
    def __init__(self):
        PackBase.__init__(self,MSG_ON_SG_GENERAL_INFO);
        self.uid    =   -1
    
    def data(self):
        """"""
        self.buf.writeInt(self.uid)
        return self.pack();
        
class com_sg_cs_GeneralRace(PackBase):
    """"""
    def __init__(self):
        """"""
        PackBase.__init__(self,MSG_ON_SG_GENERAL_RACE)
        self.uid    =   -1
        self.cid    =   0
        self.gid    =   -1
        self.race_type= 6
    
    def data(self):
        """"""
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        self.buf.writeInt(self.gid)
        self.buf.writeShort(self.race_type)
        return self.pack();
   
class com_hx_cs_GeneralRace(PackBase):
    """"""
    def __init__(self):
        """"""
        PackBase.__init__(self,MSG_ON_SG_GENERAL_RACE)
        self.uid    =   -1
        self.gid    =   -1
        self.race_type= 6
    
    def data(self):
        """"""
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.gid)
        self.buf.writeShort(self.race_type)
        return self.pack();

class com_sg_cs_GetRobCount(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_ROB_COUNT)
        self.uid    =   -1
        
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack();
        
class com_sg_cs_OnLineAwardInfo(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_AWARD_INFO)
        self.uid    = -1
        
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()

class com_hx_cs_OnLineAwardInfo(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_AWARD_INFO)
        self.uid    = -1
        
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()
        
class com_sg_cs_EncourageAward(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_ENCOURAGE_AWARD)
        self.uid    =   -1
    
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()
class com_hx_cs_EncourageAward(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_ENCOURAGE_AWARD)
        self.uid    =   -1
    
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()

class com_sg_cs_JoinBattleField(PackBase):
    """"""
    def __init__(self):
        PackBase.__init__(self,MSG_ON_SG_BATTLEFIELD);
        self.uid    =   -1
        self.cid    =   0
        self.gens   =   []
        self.guwu   =   0
        
    def data(self):
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        self.buf.writeShort(len(self.gens))
        for gid in self.gens:
            self.buf.writeInt(gid)
        self.buf.writeShort(self.guwu)
        return self.pack()
        
class com_sg_cs_BattleFieldAttack(PackBase):
    """ """
    def __init__(self):
        PackBase.__init__(self,MSG_ON_SG_BATTLEFIELD_ATTACK);
        self.uid    =   -1
        self.attacked=  ""
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        self.buf.writeShort(self.strLen(self.attacked))
        self.buf.writeUTFBytes(self.attacked)
        return self.pack()
        
class com_sg_cs_JoinBattleRace(PackBase):
    """"""
    def __init__(self):
        """"""
        PackBase.__init__(self,MSG_ON_SG_BATTLERACE)
        self.uid    =   -1
        self.cid    =   0
        self.gens   =   []
        self.guwu   =   0
        
    def data(self):
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        self.buf.writeShort(len(self.gens))
        for gid in self.gens:
            self.buf.writeInt(gid)
        self.buf.writeShort(self.guwu)
        return self.pack()

class com_sg_cs_JoinCrossBattleRace(PackBase):
    """"""
    def __init__(self):
        """"""
        PackBase.__init__(self,MSG_ON_SG_BATTLERACE)
        self.uid    =   -1
        self.cid    =   0
        self.gens   =   []
        self.ptype  =   0
        
    def data(self):
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        self.buf.writeShort(len(self.gens))
        for gid in self.gens:
            self.buf.writeInt(gid)
        self.buf.writeShort(self.ptype)
        return self.pack()

class com_hx_cs_AddGeneralBlood(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_ADD_GENERAL_BOOLD)
        self.uid    =   -1
        self.gids   =   []
    
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        self.buf.writeShort(len(self.gids))
        for gid in self.gids:
            self.buf.writeInt(gid)
        return self.pack()

class com_hx_cs_AddGoldBlood(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_ADD_GOLD_BOOLD)
        self.uid    =   -1
        self.gold   =   0
        
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.gold)
        return self.pack()
        
class com_hx_cs_GlobalMapJoinRoom(PackBase):
    """"""
    def __init__(self):
        """"""
        PackBase.__init__(self,MSG_ON_HX_GLOBALMAP_ROOM_JOIN)
        self.uid    =   -1
        self.level  =   -1
        self.guwu   =   0
        
    def data(self):
        """"""
        self.buf.writeInt(self.uid)
        self.buf.writeShort(self.level)
        self.buf.writeShort(self.guwu)
        return self.pack();

class com_hx_cs_GlobalMapLeaveRoom(PackBase):
    """"""
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_GLOBALMAP_ROOM_LEAVE)
        self.uid    =   -1
        
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()
        
class com_hx_cs_GlobalMapAttackNpc(PackBase):
    """"""
    def __init__(self):
        PackBase.__init__(self,MSG_ON_HX_GLOBALMAP_ATTACK_NPC)
        self.uid    =   -1
        self.npc    =   -1
        
    def data(self):
        """"""
        self.buf.writeInt(self.uid)
        self.buf.writeShort(self.npc)
        return self.pack()
        
class com_hx_cs_NewGlobalWarSingleStart(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_NEW_GLOBAL_WAR_SINGLE_START)
        self.uid    =   -1
        self.level  =   -1
        
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        self.buf.writeShort(self.level)
        return self.pack()
    
class com_hx_cs_NewGlobalWarSingleAttack(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_NEW_GLOBAL_WAR_SINGLE_ATTACK)
        self.uid    =   -1
    
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()
        
class com_hx_cs_NewGlobalWarTeamJoin(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_NEW_GLOBAL_WAR_TEAM_JOIN)
        self.uid    =   -1
        self.level  =   -1
    
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        self.buf.writeShort(self.level)
        return self.pack()
        
class com_hx_cs_NewGlobalWarTeamStart(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_NEW_GLOBAL_WAR_TEAM_START)
        self.uid    =   -1
    
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()
        
class com_sg_cs_onRob(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_ROB)
        self.uid    =   -1
        self.cid    =   -1
        self.rcid   =   -1
        self.gens   =   []
        self.jimou  =   0
        self.guwu   =   0
        
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        self.buf.writeInt(self.rcid)
        self.buf.writeShort(len(self.gens))
        for i in self.gens:
            self.buf.writeInt(i)
        self.buf.writeShort(self.jimou)
        self.buf.writeShort(self.guwu)
        return self.pack()
        
class com_sg_cs_refreshSkill(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_REFRESH_SKILL)
        self.uid    =   -1
        self.cid    =   -1
        
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        return self.pack();
        
class com_sg_cs_openBox(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_OPEN_BOX)
        self.uid    =   -1
        self.box    =   -1
        
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        self.buf.writeShort(self.box)
        return self.pack();
		
class com_hx_cs_onUserSkillPetCard(PackBase):
	""" """
	def __init__(self):
		""" """
		PackBase.__init__(self,MSG_ON_HX_SKILL_PET_CARD)
		self.uid	=	-1
		self.skills	=	[]
		self.pets	=	[]
	
	def data(self):
		""" """
		self.buf.writeInt(self.uid)
		self.buf.writeShort(len(self.skills))
		for skill in self.skills:
			self.buf.writeInt(skill)
		self.buf.writeShort(len(self.pets))
		for pet in self.pets:
			self.buf.writeInt(pet)
		return self.pack();
        
class com_sg_cs_onGeneralSkill(PackBase):
	""" """
	def __init__(self):
		""" """
		PackBase.__init__(self,MSG_ON_SG_GENERAL_SKILL)
		self.uid	=	-1
		self.cid	=	-1
	
	def data(self):
		""" """
		self.buf.writeInt(self.uid)
		self.buf.writeInt(self.cid)
		return self.pack()
		

class com_sg_cs_onGeneralPet(PackBase):
	""" """
	def __init__(self):
		""" """
		PackBase.__init__(self,MSG_ON_SG_GENERAL_PET)
		self.uid	=	-1
		self.cid	=	-1
	def data(self):
		""" """
		self.buf.writeInt(self.uid)
		self.buf.writeInt(self.cid)
		return self.pack()
        
class com_hx_cs_onFightJoin(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_FIGHT_JOIN);
        self.uid    =   -1
    def data(self):
        self.buf.writeInt(self.uid)
        return self.pack()
        
class com_hx_cs_onFightLeave(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_FIGHT_LEAVE);
        self.uid = -1
    def data(self):
        self.buf.writeInt(self.uid)
        return self.pack()
        
class com_hx_cs_onFightRoomPlayers(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_FIGHT_ROOM_PLAYER);
        self.uid = -1
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()

class com_hx_cs_onFightAttack(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_FIGHT_ATTACK);
        self.uid = -1
        self.name = ""
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        self.buf.writeShort(self.strLen(self.name));
        self.buf.writeUTFBytes(self.name)
        return self.pack()
class com_hx_cs_onFightRandomInvite(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_HX_FIGHT_INVITE_RONDOM);
        self.uid = -1
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()
        
class com_sg_cs_onFishStart(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_FISH_START);
        self.uid   = -1 
        self.cid   = -1
    def data(self):
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        return self.pack()

class com_sg_cs_onFishEnd(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_FISH_END);
        self.uid    = -1
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()

class com_sg_cs_onAddFishStart(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_ADD_FISH_START);
        self.uid   = -1 
        self.cid   = -1
    def data(self):
        self.buf.writeInt(self.uid)
        self.buf.writeInt(self.cid)
        return self.pack()

class com_sg_cs_onAddFishEnd(PackBase):
    """ """
    def __init__(self):
        """ """
        PackBase.__init__(self,MSG_ON_SG_ADD_FISH_END);
        self.uid    = -1
    def data(self):
        """ """
        self.buf.writeInt(self.uid)
        return self.pack()