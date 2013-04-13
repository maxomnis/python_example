#!/usr/bin/python
# -*- coding:gb2312 -*-
#=======================================================
#@author:jeffxun
#@date  : 2012/12/12
#@context: 解压消息
#=======================================================

import traceback

from messageBase import unPackBase

class com_cs_UserLogin(unPackBase):
    """ """
    def __init__(self,data):
        unPackBase.__init__(self,data)
        self.username   = ""
        self.password   = ""
        self.host       = ""
        self.gservid    = ""
        self.wservid    = ""
        self.port       = 0
    
    def unpack(self):
        """ """
        self.username = self.buf.readUTFBytes(self.buf.readShort())
        self.password = self.buf.readUTFBytes(self.buf.readShort())
        self.host     = self.buf.readUTFBytes(self.buf.readShort())
        self.gservid  = self.buf.readUTFBytes(self.buf.readShort())
        self.wservid  = self.buf.readUTFBytes(self.buf.readShort())
        self.port     = self.buf.readShort()
        return self
        
class com_cs_GeneralInfo(unPackBase):
    """ """
    def __init__(self,data):
        """"""
        unPackBase.__init__(self,data)
        self.username= ""
        self.cid    =   0
    
    def unpack(self):
        """ """
        self.username = self.buf.readUTFBytes(self.buf.readShort());
        self.cid    = self.buf.readInt();
        return self
        
class com_cs_GetTask(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.username   = ""
        self.cid        = 0
        self.task       = 0
        
    def unpack(self):
        """ """
        self.username = self.buf.readUTFBytes(self.buf.readShort());
        self.cid      = self.buf.readInt()
        self.task     = self.buf.readShort()
        return self

class com_cs_GlobalMapWar(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.username=  ""
        self.start  =   0
        self.end    =   0
        self.always =   0
        self.times  =   0
    
    def unpack(self):
        """ """
        self.username   = self.buf.readUTFBytes(self.buf.readShort());
        self.start      = self.buf.readShort()
        self.end        = self.buf.readShort()
        self.always     = self.buf.readShort()
        self.times      = self.buf.readShort()
        return self

class com_cs_NewGlobalMapWar(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.username=  ""
        self.start  =   0
        self.end    =   0
        self.always =   0
        self.times  =   0
        self.methond=   0
        self.team   =   0
    
    def unpack(self):
        """ """
        self.username   = self.buf.readUTFBytes(self.buf.readShort());
        self.start      = self.buf.readShort()
        self.end        = self.buf.readShort()
        self.always     = self.buf.readShort()
        self.times      = self.buf.readShort()
        self.methond    = self.buf.readShort()
        self.team       = self.buf.readShort()
        return self
        
class com_cs_onLineAward(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.username   = ""
        
    def unpack(self):
        """ """
        self.username   = self.buf.readUTFBytes(self.buf.readShort());
        return self

class com_cs_AutoFish(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data);
        self.username   = ""
    
    def unpack(self):
        """ """
        self.username   = self.buf.readUTFBytes(self.buf.readShort());
        return self
        
class com_cs_GeneralRace(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.username   = ""
        self.race       = 0
        self.gid        = 0
        
    def unpack(self):
        """ """
        self.username   = self.buf.readUTFBytes(self.buf.readShort());
        self.race       = self.buf.readShort()
        self.gid        = self.buf.readInt()
        return self
        
class com_cs_GeneralInfo(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.username   = ""
        self.cid        = 0
    
    def unpack(self):
        """ """
        self.username   = self.buf.readUTFBytes(self.buf.readShort());
        self.cid        = self.buf.readInt()
        return self        
        
class com_cs_BattleInfo(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.username   = ""
        self.cid        = 0
        self.battle     = 0
        self.gids       = []
        
    def unpack(self):
        """ """
        self.username   = self.buf.readUTFBytes(self.buf.readShort());
        self.cid        = self.buf.readInt()
        self.battle     = self.buf.readShort()
        num             = self.buf.readShort()
        for i in range(num):
            self.gids.append(self.buf.readInt())
    
        return self

class com_cs_onFightWar(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.username = ""
    def unpack(self):
        """ """
        self.username = self.buf.readUTFBytes(self.buf.readShort());
        return self;

        
class com_sg_sc_UserLogin(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.uid    =   -1
        self.username=  ""
        self.nickname=  ""
        
    def unpack(self):
        """ """
        self.uid    =   self.buf.readInt()
        self.username=  self.buf.readUTFBytes(self.buf.readShort())
        self.nickname=  self.buf.readUTFBytes(self.buf.readShort())
        return self;
        
class com_sg_sc_TaskInfo(unPackBase):
    """"""
    def __init__(self,data):
        """"""
        unPackBase.__init__(self,data)
        self.res    =   -1
        self.tasks  =   []
    
    def unpack(self):
        """ """
        self.res    =   self.buf.readShort()
        num =   self.buf.readShort()
        for i in range(num):
            taskid  =   self.buf.readShort()
            complete=   self.buf.readShort()
            self.tasks.append({"taskid":taskid,"complete":complete})
        return self;
            
class com_sg_sc_GeneralInfo(unPackBase):
    """"""
    def __init__(self,data):
        """"""
        unPackBase.__init__(self,data)
        self.cid    =   -1
        self.gens   =   []
    
    def unpack(self):
        """"""
        self.cid    =   self.buf.readInt()
        num         =   self.buf.readShort()
        for i in range(num):
            gid     =   self.buf.readInt()
            gtype   =   self.buf.readShort()
            pos     =   self.buf.readShort()
            gname   =   self.buf.readUTFBytes(self.buf.readShort())
            level   =   self.buf.readShort()
            power   =   self.buf.readFloat()
            forces  =   self.buf.readFloat()
            wit     =   self.buf.readFloat()
            command =   self.buf.readFloat()
            speed   =   self.buf.readFloat()
            exp     =   self.buf.readInt()
            armtype =   self.buf.readShort()
            armnum  =   self.buf.readInt()
            self.buf.readShort();
            self.buf.readShort();
            self.buf.readInt();
            self.buf.readInt();
            self.buf.readShort();
            self.gens.append({"gid":gid,"gname":gname})
        return self
        
class com_hx_sc_GeneralInfo(unPackBase):
    """"""
    def __init__(self,data):
        """"""
        unPackBase.__init__(self,data)
        self.gens   =   []
    
    def unpack(self):
        """"""
        num         =   self.buf.readShort()
        for i in range(num):
            gid     =   self.buf.readInt()
            gtype   =   self.buf.readShort()
            pos     =   self.buf.readShort()
            gname   =   self.buf.readUTFBytes(self.buf.readShort())
            level   =   self.buf.readShort()
            power   =   self.buf.readFloat()
            forces  =   self.buf.readFloat()
            wit     =   self.buf.readFloat()
            command =   self.buf.readFloat()
            speed   =   self.buf.readFloat()
            exp     =   self.buf.readInt()
            hlife   =   self.buf.readInt()
            alife   =   self.buf.readInt()
            armtype =   self.buf.readShort()
            armnum  =   self.buf.readInt()
            self.buf.readShort();
            self.buf.readShort();
            self.buf.readInt();
            self.buf.readInt();
            self.buf.readShort();
            build   =   self.buf.readShort();
            self.gens.append({"gid":gid,"gname":gname,"hlife":hlife,"alife":alife,"build":build})
        return self

class com_sg_sc_GeneralRace(unPackBase):
    """"""
    def __init__(self,data):
        """"""
        unPackBase.__init__(self,data)
        self.uid    =   -1
        self.cid    =   -1
        self.race_type  =   -1
        self.res    =   -1
        
    def unpack(self):
        """"""
        self.uid    =   self.buf.readInt()
        self.cid    =   self.buf.readInt()
        self.race_type= self.buf.readShort()
        self.res    =   self.buf.readShort()
        return self;
        
class com_hx_sc_GeneralRace(unPackBase):
    """"""
    def __init__(self,data):
        """"""
        unPackBase.__init__(self,data)
        self.uid    =   -1
        self.race_type  =   -1
        self.res    =   -1
        
    def unpack(self):
        """"""
        self.uid    =   self.buf.readInt()
        self.race_type= self.buf.readShort()
        self.res    =   self.buf.readShort()
        return self;
        
class com_sg_sc_GetRobCount(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.current_num    =   0
        self.total_num      =   0        
        
    def unpack(self):
        """ """
        self.current_num = self.buf.readShort()
        self.total_num   = self.buf.readShort()
        return self;
        
class com_sg_sc_OnLineAwardInfo(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.award_type =   -1
        self.wait_time  =   0
        self.count      =   0
        
    def unpack(self):
        """ """
        self.award_type = self.buf.readShort()
        self.wait_time  = self.buf.readInt()
        self.count      = self.buf.readShort()
        return self

class com_hx_sc_OnLineAwardInfo(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.award_type =   -1
        self.killnum    =   0
        self.Day        =   0
        self.month      =   0
        
    def unpack(self):
        """ """
        self.award_type = self.buf.readShort()
        self.killnum    = self.buf.readInt()
        self.Day        = self.buf.readShort()
        self.month      = self.buf.readShort()
        return self
        
class com_sg_sc_EncourageAward(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   -1
        self.prop   =   -1
        
    def unpack(self):
        """ """
        self.res    =   self.buf.readShort()
        self.prop   =   self.buf.readShort()
        return self

class com_hx_sc_EncourageAward(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   -1
        self.prop   =   -1
        
    def unpack(self):
        """ """
        self.res    =   self.buf.readShort()
        self.prop   =   self.buf.readShort()
        return self
        
class com_sg_sc_JoinBattleField(unPackBase):
    """"""
    def __init__(self,data):
        unPackBase.__init__(self,data)
        self.cid    =   0;
        self.res    =   0
    
    def unpack(self):
        self.res    = self.buf.readShort()
        return self

class com_sg_sc_BattleFieldStart(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.QLong  = []
        self.BHu    = []
    
    def unpack(self):
        """ """
        num = self.buf.readShort()
        for i in range(num):
            name = self.buf.readUTFBytes(self.buf.readShort());
            status= self.buf.readShort()
            if status == 1:
                self.QLong.append(name)
            elif status == 2:
                self.BHu.append(name)
            else:
                pass
        return self
        
class com_sg_sc_BattleFieldAttack(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res = -1
    def unpack(self):
        """ """
        self.res = self.buf.readShort()
        return self
        
class com_sg_sc_BattleFieldHaveAttack(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data);
        self.attack = ""
        self.alife = 0
        self.ashort = 0
        self.defend = ""
        self.dlife = 0
        self.dshort = 0
    def unpack(self):
        """ """
        self.attack = self.buf.readUTFBytes(self.buf.readShort());
        self.alife  = self.buf.readInt()
        self.ashort = self.buf.readShort()
        self.defend = self.buf.readUTFBytes(self.buf.readShort());
        self.dlife  = self.buf.readInt()
        self.dshort = self.buf.readShort()
        return self;
    
class com_sg_sc_BattleFieldEnd(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.players    = []
    def unpack(self):
        """ """
        num = self.buf.readShort()
        for i in range(num):
            rank    = self.buf.readShort()
            name    = self.buf.readUTFBytes(self.buf.readShort())
            score   = self.buf.readInt()
            self.players.append({"rank":rank,"name":name,"score":score})
        return self
        
class com_sg_sc_BattleFieldBrock(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)

    def unpack(self):
        """ """
        return self
        
class com_sg_sc_JoinBattleRace(unPackBase):
    """"""
    def __init__(self,data):
        unPackBase.__init__(self,data)
        self.cid    =   0;
        self.res    =   0
    
    def unpack(self):
        self.res    = self.buf.readShort()
        return self

class com_sg_sc_BattleRaceEnd(unPackBase):
    """ """        
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.players    =   []
    def unpack(self):
        """ """
        num = self.buf.readShort()
        for i in range(num):
            rank    = self.buf.readShort()
            name    = self.buf.readUTFBytes(self.buf.readShort())
            score   = self.buf.readShort()
            self.players.append({"rank":rank,"name":name,"score":score})
        return self
       
class com_sg_sc_BattleRaceBrock(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)

    def unpack(self):
        """ """
        return self
        
class com_sg_sc_JoinCrossBattleRace(unPackBase):
    """"""
    def __init__(self,data):
        unPackBase.__init__(self,data)
        self.cid    =   0;
        self.res    =   0
    
    def unpack(self):
        self.res    = self.buf.readShort()
        return self

class com_hx_sc_AddGeneralBlood(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   -1
        self.gens   =   []
        self.blood  = -1
    def unpack(self):
        """ """
        self.res    =   self.buf.readShort()
        num     =   self.buf.readShort()
        for i in range(num):
            gid =   self.buf.readInt()
            self.gens.append({"gid":gid})
        self.blood   = self.buf.readInt()
            
        return self

class com_hx_sc_AddGoldBlood(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   -1
        self.gold   =   -1
        self.blood  =   -1
    
    def unpack(self):
        """ """
        self.res    =   self.buf.readShort()
        self.gold   =   self.buf.readInt()
        self.blood  =   self.buf.readInt()
        return self
        
class com_hx_sc_GlobalMapJoinRoom(unPackBase):
    """"""
    def __init__(self,data):
        """"""
        unPackBase.__init__(self,data)
        self.res    =   0
        self.npcs   =   []
        
    def unpack(self):
        """"""
        self.res    =   self.buf.readShort()
        gen_num     =   self.buf.readShort()
        for i in range(gen_num):
            self.buf.readInt()
        gamer_num   =   self.buf.readShort()
        for i in range(gamer_num):
            self.buf.readUTFBytes(self.buf.readShort())
            self.buf.readInt()
            self.buf.readShort()
        npc_num     =   self.buf.readShort()
        for i in range(npc_num):
            name    =   self.buf.readUTFBytes(self.buf.readShort())
            nid     =   self.buf.readShort()            
            life    =   self.buf.readInt()
            self.npcs.append({"npc":nid,"name":name,"life":life})
        return self
        
class com_hx_sc_GlobalMapLeaveRoom(unPackBase):
    """"""
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   0
        
    def unpack(self):
        """"""
        self.res    =   self.buf.readShort()
        return self
        
class com_hx_sc_GlobalMapRoomEnd(unPackBase):
    """"""
    def __init__(self,data):
        """"""
        unPackBase.__init__(self,data)
    
    def unpack(self):
        return self

class com_hx_sc_GlobalMapAttackNpc(unPackBase):
    """"""
    def __init__(self,data):
        """"""
        unPackBase.__init__(self,data)
        self.res    =   0
    
    def unpack(self):
        self.res    =   self.buf.readShort()
        return self
        
class com_hx_sc_GlobalMapHaveAttack(unPackBase):
    """"""
    def __init__(self,data):
        unPackBase.__init__(self,data)
        self.method =   -1
        self.name   =   ""
        self.npc    =   -1
        self.life   =   -1
        
    def unpack(self):
        """"""
        self.method =   self.buf.readShort()
        self.name   =   self.buf.readUTFBytes(self.buf.readShort())
        self.buf.readInt()
        self.npc    =   self.buf.readShort()
        self.life   =   self.buf.readInt()
        self.buf.readShort()
        return self
        
class com_hx_sc_NewGlobalWarSingleStart(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   -1
        self.level  =   -1
        self.attack =   0
        self.gids   =   []
        self.npcs   =   []
        
    def unpack(self):
        """ """
        self.res  =   self.buf.readShort()
        self.level = self.buf.readShort()
        self.attack = self.buf.readShort()
        gnum    =   self.buf.readShort()
        for i in range(gnum):
            self.gids.append(self.buf.readInt())
        num =   self.buf.readShort()
        for i in range(num):
            name    =   self.buf.readUTFBytes(self.buf.readShort())
            npc     =   self.buf.readShort()
            un    =   self.buf.readShort()
            self.npcs.append({"name":name,"npc":npc,"un":un})
        return self

class com_hx_sc_NewGlobalWarSingleAttacK(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   -1
    
    def unpack(self):
        """ """
        self.res    =   self.buf.readShort()
        return self
        
class com_hx_sc_NewGlobalWarSingleAttackEd(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   -1
        self.name   =   ""
        self.life   =   0
    def unpack(self):
        """ """
        self.res    =   self.buf.readShort()
        self.name   =   self.buf.readUTFBytes(self.buf.readShort())
        self.life   =   self.buf.readInt() 
        self.npc    =   self.buf.readShort()
        self.npclife=   self.buf.readInt()
        self.buf.readShort()
        self.buf.readInt()
        self.buf.readInt()
        return self
        
class com_hx_sc_NewGlobalWarTeamJoin(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   -1
        self.master =   ""
        self.gids   =   []
        self.players=   []
    def unpack(self):
        """ """
        self.res = self.buf.readShort()
        gnum    = self.buf.readShort()
        for i in range(gnum):
            self.gids.append(self.buf.readInt())
        self.master   = self.buf.readUTFBytes(self.buf.readShort())
        num     = self.buf.readShort()
        for i in range(num):
            name = self.buf.readUTFBytes(self.buf.readShort())
            face = self.buf.readShort()
            life = self.buf.readInt()
            self.players.append({"name":name,"face":face,"life":life})
        return self
        
class com_hx_sc_NewGlobalWarTeamStart(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   -1
        self.players=   []
        self.npcs   =   []
        
    def unpack(self):
        """ """
        self.res  =   self.buf.readShort()
        pnum    =   self.buf.readShort()
        for i in range(pnum):
            name = self.buf.readUTFBytes(self.buf.readShort())
            status  = self.buf.readShort()
            self.players.append({"name":name,"status":status})
        num =   self.buf.readShort()
        for i in range(num):
            name    =   self.buf.readUTFBytes(self.buf.readShort())
            npc     =   self.buf.readShort()
            un    =   self.buf.readShort()
            self.npcs.append({"name":name,"npc":npc,"un":un})
        return self
        
class com_hx_sc_NewGlobalWarTeamOtherJoin(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.name   =   ""
        self.face   =   -1
        self.life   =   1
    def unpack(self):
        """ """
        self.name   = self.buf.readUTFBytes(self.buf.readShort())
        self.face   = self.buf.readShort()
        self.life   = self.buf.readInt()
        return self
        
class com_hx_sc_NewGlobalWarTeamOtherLeave(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.leaver = ""
        self.master = ""
        
    def unpack(self):
        """ """
        self.leaver =   self.buf.readUTFBytes(self.buf.readShort())
        self.master =   self.buf.readUTFBytes(self.buf.readShort())
        return self
    
class com_hx_sc_NewGlobalWarEnd(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.player = []
    
    def unpack(self):
        """ """
        num    = self.buf.readShort()
        for i in range(num):
            res  = self.buf.readShort()
            name = self.buf.readUTFBytes(self.buf.readShort())
            life = self.buf.readInt()
            self.buf.readInt()
            self.buf.readInt()
            self.buf.readInt()
            self.buf.readInt()
            self.buf.readInt()
            self.buf.readInt()
            self.buf.readShort()
            self.player.append({"name":name,"life":life,"res":res})
        return self
        
class com_hx_sc_NewGlobalAutoAttack(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.name   =   ""
        self.stime  =   0
        
    def unpack(self):
        """ """
        self.name = self.buf.readUTFBytes(self.buf.readShort())
        self.stime= self.buf.readInt()
        return self
        
class com_sg_sc_onRob(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.taskId =   -1
        self.cid    =   -1
        self.cname  =   ""
        self.rcid   =   -1
        self.rcname =   ""
        self.stime  =   0
        self.gens   =   []
        
    def unpack(self):
        """ """
        self.taskId = self.buf.readInt()
        self.cid    = self.buf.readInt()
        self.rcid   = self.buf.readInt()
        self.cname  = self.buf.readUTFBytes(self.buf.readShort())
        self.rcname = self.buf.readUTFBytes(self.buf.readShort())
        self.buf.readInt()
        self.stime  = self.buf.readInt()
        #---
        #self.buf.readShort()
        #num = self.buf.readShort()
        #for i in range(num):
        #    gid = self.buf.readInt()
        #    self.gens.append(gid)
        #self.buf.readShort()
        return self;
        
class com_sg_sc_refreshSkill(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res    =   -1
    
    def unpack(self):
        """ """
        cid = self.buf.readInt()
        self.res = self.buf.readShort()
        return self;
		
class com_hx_sc_onUserSkillPetCard(unPackBase):
	""" """
	def __init__(self,data):
		""" """
		unPackBase.__init__(self,data)
		self.skills	=	[]
		self.pets	=	[]
		
	def unpack(self):
		""" """
		snum = self.buf.readShort()
		for i in range(snum):
			skill = self.buf.readInt()
			self.skills.append(skill)
		pnum = self.buf.readShort()
		for i in range(pnum):
			pet = self.buf.readInt()
			self.pets.append(pet)
		return self;
		
class com_sg_sc_onGeneralSkill(unPackBase):
	""" """
	def __init__(self,data):
		""" """
		unPackBase.__init__(self,data)
		self.cid	=	-1
		self.skills = []
	
	def unpack(self):
		""" """
		self.cid = self.buf.readInt()
		num = self.buf.readShort()
		for i in range(num):
			skillid = self.buf.readInt()
			gid		= self.buf.readInt()
			stype	= self.buf.readShort()
			level   = self.buf.readShort()
			stime   = self.buf.readInt()
			self.skills.append({"skill":skillid,"gid":gid,"stype":stype,"stime":stime,"level":level})
		return self;
		
class com_sg_sc_onGeneralPet(unPackBase):
	""" """
	def __init__(self,data):
		""" """
		unPackBase.__init__(self,data)
		self.cid	=	-1
		self.pets = []
	
	def unpack(self):
		""" """
		self.cid = self.buf.readInt()
		num = self.buf.readShort()
		for i in range(num):
			petid = self.buf.readInt()
			gid		= self.buf.readInt()
			stype	= self.buf.readShort()
			level   = self.buf.readShort()
			stime   = self.buf.readInt()
			self.pets.append({"pet":petid,"gid":gid,"stype":stype,"stime":stime,"level":level})
		return self;
        
class com_hx_sc_onFightJoin(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res = -1
        self.gids = []
    def unpack(self):
        """ """
        self.res = self.buf.readShort()
        num  = self.buf.readShort()
        for i in range(num):
            gid = self.buf.readInt()
            self.gids.append(gid)
        return self;
        
class com_hx_sc_onFightOtherJoin(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data);
        self.face   = -1
        self.name   = ""
        self.life   = 0
        self.camp   = -1
    def unpack(self):
        """ """
        self.face = self.buf.readShort()
        self.name = self.buf.readUTFBytes(self.buf.readShort())
        self.life = self.buf.readInt()
        self.camp = self.buf.readShort()
        return self;
        
class com_hx_sc_onFightLeave(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data);
        self.res = -1
    def unpack(self):
        """ """
        self.res = self.buf.readShort()
        return self
        
class com_hx_sc_onFightOtherLeave(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.name = ""
    def unpack(self):
        self.name = self.buf.readUTFBytes(self.buf.readShort())
        return self;
        
class com_hx_sc_onFightRoomPlayers(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.left = []
        self.right= []
    def unpack(self):
        """ """
        num = self.buf.readShort()
        for i in range(num):
            face = self.buf.readShort()
            name = self.buf.readUTFBytes(self.buf.readShort())
            life = self.buf.readInt()
            camp = self.buf.readShort()
            if camp == 1:
                self.left.append({"name":name,"life":life,"face":face,"camp":camp})
            elif camp == 2:
                self.right.append({"name":name,"life":life,"face":face,"camp":camp})
            else:
                pass
        return self

class com_hx_sc_onFightAttack(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res = -1
    def unpack(self):
        """ """
        self.res = self.buf.readShort()
        return self;
        
class com_hx_sc_onFightHaveAttack(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.attack = ""
        self.alife  = 0
        self.defend = ""
        self.dlife  = 0
        
    def unpack(self):
        self.attack = self.buf.readUTFBytes(self.buf.readShort())
        self.alife  = self.buf.readInt()
        self.defend = self.buf.readUTFBytes(self.buf.readShort())
        self.dlife  = self.buf.readInt()
        return self;
        
class com_hx_sc_onFightRandomInvite(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.name = ""
    def unpack(self):
        """ """
        self.name = self.buf.readUTFBytes(self.buf.readShort())
        return self;
            
class com_sg_sc_onFishStart(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res = -1
        
    def unpack(self):
        """ """
        self.res = self.buf.readShort()
        return self;
        
class com_sg_sc_onFishEnd(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.uid = -1
        self.cid = -1
        self.fish_type = -1
        self.prop_type = -1
        self.num       = -1
    def unpack(self):
        """ """
        self.uid = self.buf.readInt()
        self.buf.readShort()
        self.fish_type = self.buf.readShort()
        self.prop_type = self.buf.readShort()
        self.num       = self.buf.readShort()
        self.cid       = self.buf.readInt()
        return self;

class com_sg_sc_onAddFishStart(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.res = -1
        
    def unpack(self):
        """ """
        self.res = self.buf.readShort()
        return self;
        
class com_sg_sc_onAddFishEnd(unPackBase):
    """ """
    def __init__(self,data):
        """ """
        unPackBase.__init__(self,data)
        self.uid = -1
        self.cid = -1
        self.fish_type = -1
        self.prop_type = -1
        self.num       = -1
    def unpack(self):
        """ """
        self.uid = self.buf.readInt()
        self.buf.readShort()
        self.fish_type = self.buf.readShort()
        self.prop_type = self.buf.readShort()
        self.num       = self.buf.readShort()
        self.cid       = self.buf.readInt()
        return self;
     