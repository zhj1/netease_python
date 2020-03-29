# -*- coding: utf-8 -*-
import requests
import json

headerscookies0  = {
        "Cookie": "language=cn; NTES_SESS=EyCE8GRPUXYg.N_iHeH.SosjGCTnDizuNqka6KAQTt3chQKnVhgKkIUFUUSLScQromyzxMqFU3yl.kdPqdZDW7dkTedcIhZznB6QKOSX3k8XuOMTp7kkwQ1IpZE72_PCTmjEiwKDvS9QAHdeqynhL18CPq33spIp.PyS55HWuyoJ32Jg.0.N.hAGjezzTz_a.; NTES_PASSPORT=mnOWjptnXuoQbyaNP_0Y65NY5E4j0Gk_lEw5bfAAWpt7yYwuJyZwtT6B66XSXxYMrgNYqr4tR_Nj6iOaeEsfHVjkGku4elfG6sfuvVMgmPvqVennfHDURzbXwncIs4afcrtKdu3weeedAFfhaXnfUy5fk4CT.u8sCfrEo7HX6I2Pu; S_INFO=1585287766|0|2&10##|ad_jztest509; P_INFO=ad_jztest509@163.com|1585287766|1|hongcai|00&99|bej&1577445699&hongcai#bej&null#10#0#0|&0||ad_jztest509@163.com"
      }

headerscookies1 = {
            "Cookie": "language=cn; NTES_SESS=.s58vuJpLvwd7BQ645Nt75bVJjn7.XBIkHqY4Xa_2UnVE_XDPEyXqNAdAAfMfV_C6FGkVxIk92PW_iH2f7srJJSq2QSVNE7oDK4_XIfOnq9O1IG2utqqR_BNu7.tLswg2T3.xRXFWfz3Xia7MD5WvxmvPloWgJvsXWKTmgyAgQlnClqL5xtfpt5LfV8.BjdL9; NTES_PASSPORT=HHJT18gz6.wFBUVfYGmSbQ.ZoxvbjLHKWdk9limm8owPB2k6ZBVkwenhnn.0.G2spERw.4hYbu.G7mE9p3x8d47KcK6DIzicnri6fgs1HyfXgIUUiOARqjlQLKrD6TANi0DJO1wAEbVcz57DoFL2rOFr4TjctH4GuyioGmrjMXD76; S_INFO=1585287626|0|2&10##|ad_jztest508; P_INFO=ad_jztest508@163.com|1585287626|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest508@163.com"
             }

headerscookies2 = {
        "Cookie": "language=cn; NTES_SESS=ETzGnSPR.oXhacdJvrDSsYmGLPBcFy2XEqka6KAQTt3chQKnVhgKkIUFUUSLScQroFGEcb00HO3gQ0qTSZ_bxxdkTedcIhZznB6QKOSX3k8XuOMTp7kkwQ1IpZE72_PCTmjEiwKDvS9hs6.b2GRSoBchj107QUOecS_ha_cWC79.mSnQMLO6SoimRkqhOomzx; NTES_PASSPORT=X0MTI8C7kEKscxuEySsmOF6Odsm4xjUobaBx9Lqqijyg4eB3c4CByOtDttd2dsebz7hCIemHVV2pVqFxz7MianVhrh3UvJLrtlL30ub6X10EuvwwL.RkKZETYNbGVy3uvvHe6N8I0S3fEU_KBvYczf2BGWWgWVJ0WEgrO2FjCXI53; S_INFO=1585287516|0|2&10##|ad_jztest507; P_INFO=ad_jztest507@163.com|1585287516|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest507@163.com"
       }

headerscookies3 = {
            "Cookie": "language=cn; NTES_SESS=FK2pywrBKWe3VVm1tE2UHv7iNUzVjP_42KBm3hRIHP7rDIhtCDuhBvwAwwYQYrIljYVK.FGJiDgbI2KHYcN5MMaBHOarvDcJt43Ih.YE7BiEo._HzVBByI6vzcFVeNgpHqZFLyhUSYxDBGFFNN.jo69FN3YNjLCiPQ2n4sfeGUQIyNtfpAV0lp5V3EYlbZ7bm; NTES_PASSPORT=n0GK_EYrvZNCMuRR_a8heKWP6NLd9AoE.yje2X66H_z9ZhjsWZ8jzDrVrrwKwvhSLRrSLFiPB1SN56PeLbOHyc57f7sCAQXfr0XsqxSGnJqtxAppXUuo3N2sipAyexXWt21JKVeKnKaLc4Enoyz6N4GrQAAgj_z02yBNjmE4D.6fs; S_INFO=1585287382|0|2&10##|ad_jztest506; P_INFO=ad_jztest506@163.com|1585287382|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest506@163.com"
      }

headerscookies4 = {
        "Cookie": "language=cn; NTES_SESS=zYCx5JiXunQPGh_yvOEWPfAgxzjgnB7WMrbZflGyVL0H9ylie9Ilb1MJMM3w3HyXS.cqREQej420ytrV3TkKAAjbVgjH19Tdi5fylu3p0bDpvuRV.2bb_yW1.Tz2PkQOVcYzU_lx63FTWYj2Zt_TtgMacVlSFd1v.qqZvsS5_WSVL9g0k1XlIb1kZreaan7kG; NTES_PASSPORT=qwRFoNAV2T1ASk4FA42qmEqPBgv4OdlccFy850RRfzPV1TyoG1cyPH3433EYEMT_lPN3Uf5vXbdJZRh8ljifF6ZBsBonO90s3b0oSC_uqgSKCOtt0XUwkJaan.rJoEiS82IORoFfSCwrcr74zer1pfStCirl9q5mAOa9XjT6Bn2vo; S_INFO=1585287250|0|2&10##|ad_jztest505; P_INFO=ad_jztest505@163.com|1585287250|1|hongcai|00&99|bej&1577700217&hongcai#bej&null#10#0#0|&0|hongcai|ad_jztest505@163.com"
     }

headerscookies5 = {
        "Cookie": "language=cn; NTES_SESS=k6qZ.GOygbZbjxvpwhkSBg3U2ACpVK2HaUthCw4YFopxyYwuJyZwtT6B66XSXxYMrnulkiBH4oWgY.UFX90LWWKtFaKxTy9buPCYwmXRptIRcmfFsztt3YVTs9kzd0jGFDlkv3w1HXNYFLFak42pIAtGuGq5jfTzyySa6XGatTFB9HR4gNY1YLuFz8dKYF7Yh; NTES_PASSPORT=zQfllV8ZmbzjJRHxL_NRT7o_FttUh23EJc8RAyllwTWviu82Xi.8WoQMQQZgZKuhaFLUz.sQXmFpOlGRaekwcLOxEx2_3myEQFy2PSh0zfPJS3NNyjb59HpDfAW0SY1vpQMMNawmvnx5UjYh.lbe_9K.SE405QvtzUkiLPQBVorM2; S_INFO=1585286886|0|2&10##|ad_jztest504; P_INFO=ad_jztest504@163.com|1585286886|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest504@163.com"
     }

headerscookies6 = {
        "Cookie": "language=cn; NTES_SESS=6FnceG9NXjq3TwRkXtqkEMffiJup5NhgXgCt9u7qwGxQoquJ_obuCKZ3ZZDmDQqI8GgHBNwciCdSqAgwDLHOYYnCwknQKoLfJp9quBD1xCd15BTwWMCCcqlKWL6MRHsNwPi6acujhDSLWdzAr7aJeT98tpQXKZ5XUeQKoYkQA1Jtocyg.kHajWfyM8IQCtmun; NTES_PASSPORT=jjyU4BPfk_0XxgFAFx6p133JzH0ArFodiCxqmBzzke8fM6xQ.MSx83NsNNV1VE6FT9BnwZcWV43DvzcqTIKkC_vGdGQbtHBdNaBQy0FLjiyZ0t55B7l9JOcBaBB8igDK9iMGMdqlWTXAdYS86s09Fd0Qe.InWWSDYhbSWUt_VAz2Q; S_INFO=1585286750|0|2&10##|ad_jztest503; P_INFO=ad_jztest503@163.com|1585286750|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest503@163.com"
      }

headerscookies7 = {
        "Cookie": "language=cn; NTES_SESS=rALIgTV20wUDBWZu2GArrL5syImALQuk_GMzIs9tjfvabtsWYb2sMP8l88unuatmO5QVIsJltEjHt6GjudURhhpMj7paPbdXW_ItsVucvMBceVDjHSMMitQPHdrS3U0TjJ.r4is5guKtAB26nbuOX8buQEy4nJlPt4OiFHVRu7Bl.GFYeifC2zmf826.5n0UL; NTES_PASSPORT=E3B05MNtqlPA08BLWgdi6Yqpz4bvHosmCm4MxQKKLZ1unO47rnp41.PUPPaeabO5Ju15rH38d3neCKAMJV_LmtCDlD7wSGQlP9Q72o53E62FoSyyQdkBhcHfJOkWIu2iz2tE7N2gmtE3feGwjQYXG.7a40.KXQLKkq.JtHi4efD87; S_INFO=1585286633|0|2&10##|ad_jztest502; P_INFO=ad_jztest502@163.com|1585286633|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest502@163.com"
     }

headerscookies8 = {
           "Cookie": "language=cn; NTES_SESS=3C9jLrfeLnbseptruEdDubEuXeejkTI54upPxoVKysMIjKoGNj5ophc7ccUqUIKvi_R2amCXZeToKRuyUQX.TTtpyBtIhjQ0GzxKo4U6Mpa684Hyf_pprK9hfQ3_kXbWygL3mroZDUYQ7KXRHO.pQuAxlmKfwyRA1qT2auZXGiJOjwCjDZrm7EYdPtmjsUgNg; NTES_PASSPORT=ld2NorD_WxK9Xu_ns6OcaF1pGoQIZUtPxGWUDPbbtaIOfCWYqfXWIp2i22JVJkCBFTS0GQtl7MSoHbxUFTwtG0H8K8YLoAPK2hPY7.BSlv79.oQQPz_N5mSCUwTPYaOnygaJTseOyFJExUW.NqAamhSvybvtEgfgKKac2JSHA47HY; S_INFO=1585286415|0|2&10##|ad_jztest501; P_INFO=ad_jztest501@163.com|1585286415|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0|accurate_app|ad_jztest501@163.com"
       }

headerscookies9 = {
            "Cookie":"language=cn; NTES_SESS=rN1S6k27T0PuGrq8FgvLCkpktHshj.YP9GMzIs9tjfvabtsWYb2sMP8l88unuatmO9XqtL01ONa2t6GjudURhhpMj7paPbdXW_ItsVucvMBceVDjHSMMitQPHdrS3U0TjJ.r4is5guKdNHV7ORSvVtufSoF9WOAvyLbbs1s3egyXWnULTUgf3gYZmTQxwFLnq; NTES_PASSPORT=uTiVbh4PX_R.7Iax7K7fpADTpadaG4E6T7ladRCCA0bN9ylie9Ilb1MJMM3w3HyXSo.4cXLKSJfpQCjaSLmA7xQzOziG4YROM.RiUWX8u5UoW4ssR6crp2qYVxVJrKUYu6JKyE_hiETkBTctfs30wCoAhdvnlhc52BpGionrbdYJi; S_INFO=1585285893|0|2&10##|ad_jztest500; P_INFO=ad_jztest500@163.com|1585285893|1|hongcai|00&99|bej&1577759954&hongcai#bej&null#10#0#0|&0|caiho"
}
headerscookies10 = {
            "Cookie":"language=cn; NTES_SESS=u_58DHzlNEuXFkTcEKOt704FnJUxcdcRwD9DP.lOS4_2pRC9Lp_CckbVS_tVngnsPl4B4kPhwMI0rE4P180wqt_dn7hiOjKtZzKXJswzTYte6t31R2UWvAObv7Q6eG5ZMG36dbQJTlpM24dkjiXJ8pSA7HCmVzcyA6vep28COChw4DfQs2Xpo0LuDDwGTLH3M; NTES_PASSPORT=Gg5mKoQq5WrSEHC2l87C86us4Xj1PxF7R41rzCAJ_Y9MQjLOFQaL0ZTiBa9ilMlYx3gnoShy5Ap27kocOzglgaBvqAkeXt9_Ydk5VdbAp9kRIsQja4zWD7TcpXBTONnu_GwLstuah0w1iBIMPvx85RPEcD17BpiamNOdDbiyQdVvO; S_INFO=1585293390|0|2&10##|montest13; P_INFO=montest13@163.com|1585293390|1|hongcai|00&99|bej&1577947035&hongcai#bej&null#10#0#0|&0||montest13@163.com",
}
headerscookies11 = {
        "Cookie": "language=cn; NTES_SESS=kplSAdO_9NLfc9Urc4JNwDB5X1XDc3upHUthCw4YFopxyYwuJyZwtT6B66XSXxYMr0dbNX.XBe0EWzgUIwY8879tFaKxTy9buPCYwmXRptIRcmfFsztt3YVTs9kzd0jGFDlkv3w1HXNyDXT96ru4p1oC9pWbsjR6b27EOnA_mpYp3glF3VHIJg1avIsX8AvIN; NTES_PASSPORT=.WOZn3o12moW0YoXcENnAPZN4mi8gnKkfThGJ_XXM7B1DIhtCDuhBvwAwwYQYrIlj0ezkb0..kYeolCFc3buNtgFpFtRfZ_pwz_tL6ln.4Ld6fkk_SqKEVafipFyg.r9LDxMIwLoRLIhFE5kTvSns5gujAjDfsa6iotrnHON7YL3t; S_INFO=1585293637|0|2&10##|ad_jztest400; P_INFO=ad_jztest400@163.com|1585293637|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||ad_jztest400@163.com",
}
headerscookies12 = {
            "Cookie": "language=cn; NTES_SESS=.M7CbQpZXmkmdmPidcaD_qv2oSnC_Erp9iDiezhpjfyVE_XDPEyXqN0uV9yiIoHcF700Y1IfpqSzRI0t0jbQWiaKpLUIH1LtsyvDEBWxuVp2P4hKRWFREe4gqmxOxcc6IPS4HarVy0zrDbXSR_gg2V4lHQcD9LN3hECbZqZoLiPbaLOtL.pztC9L88UtrFeHy; NTES_PASSPORT=FIQJRSlGPdakTgD9LuEHHzxy2Eq9xZ62cNQmXT9EUoKDt.nVltzn6dqx52zHFM4WPXp7ushigazQCtDlpsVGpCzQqBTriyYK1PIGYuy8D.hNWU0aB_2CbOphLgqbVMGi9HAmLipUFIA8AtN2cCng9N8eg0U8BwAe0UFdasxDwLJwV; S_INFO=1585293831|0|2&10##|montest299; P_INFO=montest299@163.com|1585293831|1|hongcai|00&99|bej&1584598353&hongcai#bej&null#10#0#0|&0||montest299@163.com",
}
headerscookies13 = {
            "Cookie": "language=cn; NTES_SESS=WPhX8ctQJchPA67cpf.zhp1PMrqvBTO6YJdJ_6.1n9qwvcIdRvqIer10eYy6liGjYx2amZWhXRSvP6Mnw_Be3xF3xLzA10pM2SpuYHsSPtMy8Mi5cwGh4Z1X4Lk8yTE2mTi83XkYP.vuA1sk3iJWSdKWIFK5veWfoBF31ezaqwAMdtwgVtCTooRWJJsTPRgim; NTES_PASSPORT=9V5LzlQD1MaAAE974qaZO1AUb9LrJiNWvyPGrZhli.b80pfTK0EfvznQve4tJ_rVeuKF0N3j5MxXN01.q3_W3PNeAhUYm6bi.XU_jXMhcbUD2x0pEyrQBoBqP4YgbylOlMDVGLCLztPskgb0Fdrolag2DpuzSTA85HITyQxSVkZuT; S_INFO=1585293933|0|2&10##|montest96; P_INFO=montest96@163.com|1585293933|1|hongcai|00&99|bej&1578554518&hongcai#bej&null#10#0#0|&0||montest96@163.com",
}
headerscookies14 = {
        "Cookie": "language=cn; NTES_SESS=I7OY8JKXjaS9uzq0sk.RMoTYSe33i9Ft19E9LuXg65RtOGeEUOReTsbnfraKGowlZxzFswZZG9rXy38xQWc8D7p6YPSK878Q2NHl3NTfsFVsOrnT1ucNukrnnHxNW7OIIY.TA42HZUmLej3p.SdJjfK2nVqtGcxtTTPdR0H9nZW6M_4Et70NqI3CwaI.gZnrL; NTES_PASSPORT=zQkSYyDhSUp7uNVEnVMHs9CBjwvei_23nt39GzksWHMNvcIdRvqIerlUipTEc3kzVxH8kvY8xVC_WsftD1pajaCPT4_Vi_C8QxslOqE6kQi2gzUMc6lJtDmm3Ze2ipQlfeaCjW5m62Qh1sasldBMiZzTQuhZ08yfAwJrQjUIJqZYF.lG1Vwn2HuB2; S_INFO=1585294040|0|2&10##|hongcaitest456; P_INFO=hongcaitest456@163.com|1585294040|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||hongcaitest456@163.com",
}
headerscookies15 = {
            # "Cookie":"language=cn; NTES_SESS=rN1S6k27T0PuGrq8FgvLCkpktHshj.YP9GMzIs9tjfvabtsWYb2sMP8l88unuatmO9XqtL01ONa2t6GjudURhhpMj7paPbdXW_ItsVucvMBceVDjHSMMitQPHdrS3U0TjJ.r4is5guKdNHV7ORSvVtufSoF9WOAvyLbbs1s3egyXWnULTUgf3gYZmTQxwFLnq; NTES_PASSPORT=uTiVbh4PX_R.7Iax7K7fpADTpadaG4E6T7ladRCCA0bN9ylie9Ilb1MJMM3w3HyXSo.4cXLKSJfpQCjaSLmA7xQzOziG4YROM.RiUWX8u5UoW4ssR6crp2qYVxVJrKUYu6JKyE_hiETkBTctfs30wCoAhdvnlhc52BpGionrbdYJi; S_INFO=1585285893|0|2&10##|ad_jztest500; P_INFO=ad_jztest500@163.com|1585285893|1|hongcai|00&99|bej&1577759954&hongcai#bej&null#10#0#0|&0|caiho"
        "Cookie": "language=cn; NTES_SESS=r25n1gMSSx.Tlmbbfi05GME4qXeXkepyY6W6ZKNqEu2abtsWYb2sMPgdzyiIthT1URMRgAJr3sMada.9aovjRZb0UOFvrVnEZC_1FCMzPfRPbydMXKwCKeydd_3CpAbrrx5M0.G_UYLZsLtcpW2OsDzWpVQRhfjM1VoH4AD4GjPHk34tXG7A5tiJlOT01bsH3; NTES_PASSPORT=gh4AIQOZ7dAVYNQmEp_QIbq3h9s7B0TWxhBCogajs0zG_3MId_YMi7VElPfe3Bagnqbs0JDSVzeAxAbZuHuuhJtDfqJnlJtrxpjVLYekaxl8UgEz3kVuhXD7SQY3Y2Uh8b_Bp7cOklZHJm1zvSQOpxwhpX7eViu.3VD5cAdgMC7.JwrhUHlNIK4m8; S_INFO=1585294128|0|2&10##|hongcaitest999; P_INFO=hongcaitest999@163.com|1585294128|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0|accurate_app|hongcaitest999@163.com",
}
headerscookies16 = {
            # "Cookie":"language=cn; NTES_SESS=rN1S6k27T0PuGrq8FgvLCkpktHshj.YP9GMzIs9tjfvabtsWYb2sMP8l88unuatmO9XqtL01ONa2t6GjudURhhpMj7paPbdXW_ItsVucvMBceVDjHSMMitQPHdrS3U0TjJ.r4is5guKdNHV7ORSvVtufSoF9WOAvyLbbs1s3egyXWnULTUgf3gYZmTQxwFLnq; NTES_PASSPORT=uTiVbh4PX_R.7Iax7K7fpADTpadaG4E6T7ladRCCA0bN9ylie9Ilb1MJMM3w3HyXSo.4cXLKSJfpQCjaSLmA7xQzOziG4YROM.RiUWX8u5UoW4ssR6crp2qYVxVJrKUYu6JKyE_hiETkBTctfs30wCoAhdvnlhc52BpGionrbdYJi; S_INFO=1585285893|0|2&10##|ad_jztest500; P_INFO=ad_jztest500@163.com|1585285893|1|hongcai|00&99|bej&1577759954&hongcai#bej&null#10#0#0|&0|caiho"
    "Cookie": "language=cn; NTES_SESS=RPhenCFdrtwZsuntC_yuHwev28OBRXJEdmZmB0jfLAlEwsISwc4gjpotVVAHANXWxG.Mimv3sm.eMFXuoU2M2aPofqch19qsOlDZ3zFT8NfkbJjoCF7C3BVtTY05TL9LXbUJ1PvNlR0vo3Dl7jEtbLqmEiLSH96ovVm_BN9mc2rs1sea3bRzGOcxnJhmoVLJ7gNocD5xs1Btp; NTES_PASSPORT=wikam4sUGwv6BSolJAakKxpZ1z6w3uVttWIqEHxFwjhcBlf2BpU6Vj7yuuq.q8dislHKcGRPWSl4adswDZ.LphrIK4HlL1Th6gvsTo1iUdDWfw2m4Nep5._JwXWHk0x5Xh0cLk4pLnx.DIXhAxzXg1OhQDsIl7_5s68xtPz0tPTUSOa6fdqYsIbBlXyZF90AP; S_INFO=1585294219|0|2&70##|ad_jztest1; P_INFO=ad_jztest1@163.com|1585294219|1|hongcai|00&99|bej&1579056735&hongcai#bej&null#10#0#0|&0|accurate_app|ad_jztest1@163.com",
}
headerscookies17 = {
            # "Cookie":"language=cn; NTES_SESS=rN1S6k27T0PuGrq8FgvLCkpktHshj.YP9GMzIs9tjfvabtsWYb2sMP8l88unuatmO9XqtL01ONa2t6GjudURhhpMj7paPbdXW_ItsVucvMBceVDjHSMMitQPHdrS3U0TjJ.r4is5guKdNHV7ORSvVtufSoF9WOAvyLbbs1s3egyXWnULTUgf3gYZmTQxwFLnq; NTES_PASSPORT=uTiVbh4PX_R.7Iax7K7fpADTpadaG4E6T7ladRCCA0bN9ylie9Ilb1MJMM3w3HyXSo.4cXLKSJfpQCjaSLmA7xQzOziG4YROM.RiUWX8u5UoW4ssR6crp2qYVxVJrKUYu6JKyE_hiETkBTctfs30wCoAhdvnlhc52BpGionrbdYJi; S_INFO=1585285893|0|2&10##|ad_jztest500; P_INFO=ad_jztest500@163.com|1585285893|1|hongcai|00&99|bej&1577759954&hongcai#bej&null#10#0#0|&0|caiho"
"Cookie": "language=cn; NTES_SESS=2DyCQFAJeqUlATxYintoK_Ub7_9a009RTbqbfVm7g_D6T9Yq4TDYdx7OdX3VMI5rX99VmSWNPOh_oVWg6ftdCNkCNvsB7OGW.HGZXF8HouW3QWIL965wPl7APvnQ3ER.haoKU3R8WLGl2hMEpR1FfZlQlmjSwMPgfDFN.5kz9JUstggLM7DaJuN2bb8Eo4jIh; NTES_PASSPORT=nC40wf_wv_gkUoSaIHagiaVwL9oBygDtaOHwBRf47913ZhjsWZ8jzDYCzrSTUgBqrFsvLZ4hnV_DuZ.9NagoaHurLf2G_d17952gA5Pfk120ctZh8OBCvFx3ctHxsKVFsrYeNru07j2CekkNHbcwJd0tT40Sku0niMjaVwGERQwVs; S_INFO=1585294295|0|2&10##|montest93; P_INFO=montest93@163.com|1585294295|1|hongcai|00&99|null&null&null#bej&null#10#0#0|&0||montest93@163.com",
}
headerscookies18 = {
            # "Cookie":"language=cn; NTES_SESS=rN1S6k27T0PuGrq8FgvLCkpktHshj.YP9GMzIs9tjfvabtsWYb2sMP8l88unuatmO9XqtL01ONa2t6GjudURhhpMj7paPbdXW_ItsVucvMBceVDjHSMMitQPHdrS3U0TjJ.r4is5guKdNHV7ORSvVtufSoF9WOAvyLbbs1s3egyXWnULTUgf3gYZmTQxwFLnq; NTES_PASSPORT=uTiVbh4PX_R.7Iax7K7fpADTpadaG4E6T7ladRCCA0bN9ylie9Ilb1MJMM3w3HyXSo.4cXLKSJfpQCjaSLmA7xQzOziG4YROM.RiUWX8u5UoW4ssR6crp2qYVxVJrKUYu6JKyE_hiETkBTctfs30wCoAhdvnlhc52BpGionrbdYJi; S_INFO=1585285893|0|2&10##|ad_jztest500; P_INFO=ad_jztest500@163.com|1585285893|1|hongcai|00&99|bej&1577759954&hongcai#bej&null#10#0#0|&0|caiho"
"Cookie": "language=cn; NTES_SESS=kZjyTMFc_8UXBqD8dpU6OgSqm7RXhcbz2.u.ANg_5XZxyYwuJyZwtTW3qiq1Z.J_JMwzgoTT5KpxVGwHH4dkTMZWEDOz_4eFn1eQ67a1i8FMKFhqYxdrbS_VbDGKM3CnjPiocMCaFqerE1BCjQU48QfeX_CoZoh46Dl_Qxr_1_Fb8fwqObuHw2mk..a3iJLhj; NTES_PASSPORT=7d8yHkgwqU2vru5CMc5WQaJPzMBSZgAcOEKg6yY3cioZsnGNSs0GxtK8VFVb01SmSylBpT1vNv_rcc4EH38W7Sz5eYH_IAocifHpwfCY1oHTbVsn0E6ldUuWlEnmux_3YjeYbgq.eCcZtF9Hb_plxxvnH.NA_IZ9hPWVWeqYAyqDN; S_INFO=1585294349|0|2&10##|montest30; P_INFO=montest30@163.com|1585294349|1|hongcai|00&99|bej&1578282589&hongcai#bej&null#10#0#0|&0||montest30@163.com",

}
headerscookies19 = {
            # "Cookie":"language=cn; NTES_SESS=rN1S6k27T0PuGrq8FgvLCkpktHshj.YP9GMzIs9tjfvabtsWYb2sMP8l88unuatmO9XqtL01ONa2t6GjudURhhpMj7paPbdXW_ItsVucvMBceVDjHSMMitQPHdrS3U0TjJ.r4is5guKdNHV7ORSvVtufSoF9WOAvyLbbs1s3egyXWnULTUgf3gYZmTQxwFLnq; NTES_PASSPORT=uTiVbh4PX_R.7Iax7K7fpADTpadaG4E6T7ladRCCA0bN9ylie9Ilb1MJMM3w3HyXSo.4cXLKSJfpQCjaSLmA7xQzOziG4YROM.RiUWX8u5UoW4ssR6crp2qYVxVJrKUYu6JKyE_hiETkBTctfs30wCoAhdvnlhc52BpGionrbdYJi; S_INFO=1585285893|0|2&10##|ad_jztest500; P_INFO=ad_jztest500@163.com|1585285893|1|hongcai|00&99|bej&1577759954&hongcai#bej&null#10#0#0|&0|caiho"
"Cookie": "language=cn; NTES_SESS=yEFEWLag6dBrAmuY4ujHYCZek8aR8g7jJksk6TGYew8DgN.agb3pG9df3.2Vh1aQBctm7zOsiHu8BJTi3_ntEr8HyuRNYCA1pcAar94c.O1wanQtGtuQ8rOx2ufPSlMp5J.biSM41tALCr1zU1KChaTt1dTEy4puUHFsjR3I4vky0SnNEVAlanUjA617YCxJwmdL0EL_rEI19; NTES_PASSPORT=FrOp9v.SPDK2xpXg5Tm1wPiTgLaCaO8B72YDRFNk6rw9tMe.tG1VzrON1ef3qw.iRwgqZ7hlFCN9RHoZVrYEq.IZ8NfzxOw6rsftEsnNAwfWj4oqb2R7QXvVNNsZmq5IuGALliLbapXtk8UjqcueqLyZ9M_8bh_lzPuQYMmGalnEVvrnogSIer.WV; S_INFO=1585294414|0|2&70##|montest85; P_INFO=montest85@163.com|1585294414|1|hongcai|00&99|bej&1585200913&openid#bej&null#10#0#0|&0|openid|montest85@163.com",
}


# list = [headerscookies0,headerscookies1,headerscookies2,headerscookies3,headerscookies4,headerscookies5,headerscookies6,headerscookies7,headerscookies8,headerscookies9,headerscookies10,headerscookies11,headerscookies12,headerscookies13,headerscookies14,headerscookies15,headerscookies16,headerscookies17,headerscookies18,headerscookies19]
list = [headerscookies10,headerscookies11,headerscookies12,headerscookies13,headerscookies14,headerscookies15,headerscookies16,headerscookies17,headerscookies18,headerscookies19]

# post_publicThread = "https://hc-expert-test.ws.netease.com/api/proficient/thread/addThread"

def post_pathSpecial():
    params_publicThread = {
        "categoryId": "1",
        "title": "精准比分——自动化测试发文",
        "price": "28",
        "matches": '[{"matchInfoId":1000000000582324,"recommendPlayList":[{"playId":1000000000591309,"predictItemIds":[1000000001177060],"playMetaId":1}]},{"matchInfoId":1000000000582325,"recommendPlayList":[{"playId":1000000000591312,"predictItemIds":[1000000001177069],"playMetaId":2}]}]',
        "content": "精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比准精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精准比分精准比分精准比分vv精准比分精准比分精准比分精准比分精准比分精",
        # "buyReason": "自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发自动化测试发文自动化测试发文自动化测试发自动化测试发文自动化测试发文自动化测试发自动化测试发文自动化测试发文自动化测试发自动化测试发文自动化测试发文自动化测试发自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文自动化测试发文",
        "isTempSave": "0"
        # "businessTypeId": "0"
    }
    params = params_publicThread
    path_name = "https://hc-expert-test.ws.netease.com/api/proficient/thread/addThread"
    for i in list:
        headers = i
        print(i)
        res = requests.post(path_name, params=params, headers=headers, verify=False)
        # res = requests.post(path_name, params=params, headers=headers, verify=False)
        print(res.text)
    return


post_pathSpecial()
