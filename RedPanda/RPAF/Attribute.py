from OCC.Core.TFunction import TFunction_Logbook
from OCC.Core.TDF import (
    TDF_LabelMap,
    TDF_Label,
    TDF_Attribute
)

from OCC.Core.TDataStd import (
    TDataStd_Name,
    TDataStd_Real,
    TDataStd_Integer,
    TDataStd_TreeNode,
    TDataStd_Comment
)
from OCC.Core.TNaming import (
    TNaming_NamedShape,
    TNaming_Builder
)
from OCC.Core.TPrsStd import (
    TPrsStd_AISPresentation,
    TPrsStd_AISViewer,
)
from OCC.Core.TFunction import (
    TFunction_Function,
)
from OCC.Core.XCAFDoc import (
    XCAFDoc_Location,
)
from .GUID import *


def Comment_Get(comment_Attr:TDataStd_Comment):
    import re
    pattern = re.compile(".*Comment=\|(.*)\|", re.S)
    comment0 = pattern.match(comment_Attr.DumpToString())
    return comment0.group(1)
    
TDataStd_Comment.Get = Comment_Get

class Attr_Assembly(TDataStd_TreeNode):
    def GetID():
        return AssemblyGUID

class Attr_ShapeRef(TDataStd_TreeNode):
    """
    label0 ref Label1.Shape
    => label0 is Label1.Shape
    """

    def SetReference(self, theLabel:TDF_Label):
        father = Attr_ShapeRef.Set(theLabel)
        father.Append(Attr_ShapeRef)

    def Get(self):
        father = self.Father()
        if father:
            return father.Label()
        return None

    @staticmethod
    def Set(aLabel, theRefedLabel=None)->TDataStd_TreeNode:
        TN_self = TDataStd_TreeNode.Set(aLabel, Attr_ShapeRef.GetID())
        TN_self.__class__ = Attr_ShapeRef
        if theRefedLabel:
            # TODO: solve round ref
            father = Attr_ShapeRef.Set(theRefedLabel)
            father.Append(TN_self)
        return TN_self

    @staticmethod
    def GetID():
        return ShapeRefGUID

    def __iter__(self):
        self.it = self.First()
        return self

    def __next__(self):
        if self.it is None:
            raise StopIteration

        node = self.it
        self.it = node.Next()
        return node.Label()

class Attr_Guid(TFunction_Function):
    @staticmethod
    def GetID():
        return Sym_IdAttr_GUID

class Attr_IDcol(TDataStd_TreeNode):
    def GetID():
        return IDcolGUID

class Attr_IDcolSurf(TDataStd_TreeNode):
    def GetID():
        return IDcolSurfGUID

class Attr_IDcolCurv(TDataStd_TreeNode):
    def GetID():
        return IDcolCurvGUID

class Attr_StateMessage(TDataStd_Comment):
    def GetID():
        return TDataStd_Comment.GetID()


class DFAttr_LogBook(TFunction_Logbook):
    def __init__(self) -> None:
        super().__init__()

    # TFunction_Logbook
    def SetUnTouched(self:TFunction_Logbook, theLabel:TDF_Label):
        map_Lab:TDF_LabelMap = self.GetTouched()
        map_Lab.remove(theLabel)

    def SetUnImpacted(self:TFunction_Logbook, theLabel:TDF_Label):
        map_Lab:TDF_LabelMap = self.GetImpacted()
        map_Lab.remove(theLabel)

    def SetUnValid(self:TFunction_Logbook, theLabel:TDF_Label):
        map_Lab:TDF_LabelMap = self.GetValid()
        map_Lab.remove(theLabel)


from .Attr.State import Attr_State, Attr_Exist
attr_li = [
    TDataStd_Name,
    TDataStd_Real,
    TDataStd_Integer,
    TNaming_NamedShape,
    TPrsStd_AISPresentation,
    TPrsStd_AISViewer,
    TFunction_Function,
    XCAFDoc_Location,

    DFAttr_LogBook,
    Attr_Assembly,
    Attr_ShapeRef,
    Attr_Guid,
    Attr_IDcol,
    Attr_IDcolSurf,
    Attr_IDcolCurv,
    Attr_State,
    Attr_Exist,
    Attr_StateMessage,
]

Lookup_Attr = GuidLookup(map(lambda x:x.GetID(), attr_li), attr_li)



# data translate
def FromText(theType:type, text:str):
    if theType == TDataStd_Real:
        from math import pi
        try:
            num = eval(text)
            if isinstance(num, int) or isinstance(num, float):
                return num
        except:
            pass
        return 0.0
    elif theType == TDataStd_Integer:
        return int(text)

    return text
