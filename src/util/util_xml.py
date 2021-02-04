# coding=utf-8
import xml.etree.ElementTree as ET


def get_xml_root(path):
    '''
    通过path获取xml的root解析
    :param path:
    :return:
    '''
    try:
        tree = ET.parse(path)
    except Exception as ret:
        raise Exception("解析xml是发生异常，请检查xml格式")

    return tree, tree.getroot()


def get_project_config(xml_path="./config/project.xml", type="local"):
    '''
    通过指定参数获取指定项目配置
    :param path:
    :return:
    '''
    res, result = [], {}
    tree, root = get_xml_root(xml_path)
    for child in root:
        if child.get("type") == "local":
            for c in child:
                if c.get("enable") == "True":
                    result["name"] = c.get("name")
                    result["version"] = c.get("version")
                    result["enable"] = c.get("enable")
                    res.append(result)
    return res


def get_phone_config(xml_path="./config/phone.xml", type="local", enable="True"):
    '''
    通过指定参数获取指定位置的机型信息
    :param xml_path:
    :return:
    '''
    res = list()
    tree, root = get_xml_root(xml_path)
    # 遍历xml所有节点
    for child in root:
        if child.get("type") == "local" and enable == "True":
            for c in child:
                result = {}
                result["band"] = c.text
                result["deviceName"] = c.get("deviceName")
                result["platformName"] = c.get("platformName")
                result["platformVersion"] = c.get("platformVersion")
                result["appPackage"] = c.get("appPackage")
                result["appActivity"] = c.get("appActivity")
                res.append(result)
    return res


if __name__ == "__main__":
    print(get_project_config())
    print(get_phone_config())
