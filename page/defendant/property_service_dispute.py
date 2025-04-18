import streamlit as st
import json
from page.components.defendant import Respondent
from page.components.header import header
from utils.document_generator import DocumentGenerator, BaseCaseFormatter
import logging
import pandas as pd
from datetime import date, datetime
from page.components.ai_ui import AIComponent

logger = logging.getLogger(__name__)

CASE_TYPE = '物业服务合同纠纷'

ai_component = AIComponent(CASE_TYPE)


def respondent_details(thisCase: dict):
    # 1. 对物业费有无异议
    st.subheader("1. 对物业费有无异议")
    q1_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="q1_options", horizontal=True)
    if q1_options == "无":
        q1_detail = f'无☑\n有☐ 事实和理由：'
    else:
        q1_fact = st.text_area("事实和理由", key="q1_fact")
        ai_component.ai_optimize_text(
            q1_fact, id="q1_fact_b", isDefendant=True)
        q1_detail = f'无☐\n有☑ 事实和理由：{q1_fact}'
    thisCase.reply_matters.append(q1_detail)

    # 2. 对违约金有无异议
    st.subheader("2. 对违约金有无异议")
    q2_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="q2_options", horizontal=True)
    if q2_options == "无":
        q2_detail = f'无☑\n有☐ 事实和理由：'
    else:
        q2_fact = st.text_area("事实和理由", key="q2_fact")
        ai_component.ai_optimize_text(
            q2_fact, id="q2_fact_b", isDefendant=True)
        q2_detail = f'无☐\n有☑ 事实和理由：{q2_fact}'
    thisCase.reply_matters.append(q2_detail)

    # 3. 对其他请求有无异议
    st.subheader("3. 对其他请求有无异议")
    q3_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="q3_options", horizontal=True)
    if q3_options == "无":
        q3_detail = f'无☑\n有☐ 事实和理由：'
    else:
        q3_fact = st.text_area("事实和理由", key="q3_fact")
        ai_component.ai_optimize_text(
            q3_fact, id="q3_fact_b", isDefendant=True)
        q3_detail = f'无☐\n有☑ 事实和理由：{q3_fact}'
    thisCase.reply_matters.append(q3_detail)

    # 4. 对标的总额有无异议
    st.subheader("4. 对标的总额有无异议")
    q4_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="q4_options", horizontal=True)
    if q4_options == "无":
        q4_detail = f'无☑\n有☐ 事实和理由：'
    else:
        q4_fact = st.text_area("事实和理由", key="q4_fact")
        ai_component.ai_optimize_text(
            q4_fact, id="q4_fact_b", isDefendant=True)
        q4_detail = f'无☐\n有☑ 事实和理由：{q4_fact}'
    thisCase.reply_matters.append(q4_detail)

    # 5. 答辩依据
    st.subheader("5. 答辩依据")
    q5_1 = st.text_area("合同约定", key="q5_1")
    q5_2 = st.text_area("法律规定", key="q5_2")
    q5_detail = f'合同约定：{q5_1}\n法律规定：{q5_2}'
    thisCase.reply_matters.append(q5_detail)


def fact_reason(thisCase: dict):
    # 1. 对物业服务合同或前期物业服务合同签订情况有无异议
    st.subheader("1. 对物业服务合同或前期物业服务合同签订情况（名称、编号、签订时间、地点等）有无异议")
    f1_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="f1_options", horizontal=True)
    if f1_options == "无":
        f1_detail = f'无☑\n有☐ 事实和理由：'
    else:
        f1_fact = st.text_area("事实和理由", key="f1_fact")
        ai_component.ai_optimize_text(
            f1_fact, id="f1_fact_b", isDefendant=True)
        f1_detail = f'无☐\n有☑ 事实和理由：{f1_fact}'
    thisCase.reasons.append(f1_detail)

    # 2. 对签订主体有无异议
    st.subheader("2. 对签订主体有无异议")
    f2_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="f2_options", horizontal=True)
    if f2_options == "无":
        f2_detail = f'无☑\n有☐ 事实和理由：'
    else:
        f2_fact = st.text_area("事实和理由", key="f2_fact")
        ai_component.ai_optimize_text(
            f2_fact, id="f2_fact_b", isDefendant=True)
        f2_detail = f'无☐\n有☑ 事实和理由：{f2_fact}'
    thisCase.reasons.append(f2_detail)

    # 3. 对物业项目情况有无异议
    st.subheader("3. 对物业项目情况有无异议")
    f3_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="f3_options", horizontal=True)
    if f3_options == "无":
        f3_detail = f'无☑\n有☐ 事实和理由：'
    else:
        f3_fact = st.text_area("事实和理由", key="f3_fact")
        ai_component.ai_optimize_text(
            f3_fact, id="f3_fact_b", isDefendant=True)
        f3_detail = f'无☐\n有☑ 事实和理由：{f3_fact}'
    thisCase.reasons.append(f3_detail)

    # 4. 对物业费标准有无异议
    st.subheader("4. 对物业费标准有无异议")
    f4_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="f4_options", horizontal=True)
    if f4_options == "无":
        f4_detail = f'无☑\n有☐ 事实和理由：'
    else:
        f4_fact = st.text_area("事实和理由", key="f4_fact")
        ai_component.ai_optimize_text(
            f4_fact, id="f4_fact_b", isDefendant=True)
        f4_detail = f'无☐\n有☑ 事实和理由：{f4_fact}'
    thisCase.reasons.append(f4_detail)

    # 5. 对物业服务期限有无异议
    st.subheader("5. 对物业服务期限有无异议")
    f5_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="f5_options", horizontal=True)
    if f5_options == "无":
        f5_detail = f'无☑\n有☐ 事实和理由：'
    else:
        f5_fact = st.text_area("事实和理由", key="f5_fact")
        ai_component.ai_optimize_text(
            f5_fact, id="f5_fact_b", isDefendant=True)
        f5_detail = f'无☐\n有☑ 事实和理由：{f5_fact}'
    thisCase.reasons.append(f5_detail)

    # 6. 对物业费支付方式有无异议
    st.subheader("6. 对物业费支付方式有无异议")
    f6_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="f6_options", horizontal=True)
    if f6_options == "无":
        f6_detail = f'无☑\n有☐ 事实和理由：'
    else:
        f6_fact = st.text_area("事实和理由", key="f6_fact")
        ai_component.ai_optimize_text(
            f6_fact, id="f6_fact_b", isDefendant=True)
        f6_detail = f'无☐\n有☑ 事实和理由：{f6_fact}'
    thisCase.reasons.append(f6_detail)

    # 7. 对逾期支付物业费违约金标准有无异议
    st.subheader("7. 对逾期支付物业费违约金标准有无异议")
    f7_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="f7_options", horizontal=True)
    if f7_options == "无":
        f7_detail = f'无☑\n有☐ 事实和理由：'
    else:
        f7_fact = st.text_area("事实和理由", key="f7_fact")
        ai_component.ai_optimize_text(
            f7_fact, id="f7_fact_b", isDefendant=True)
        f7_detail = f'无☐\n有☑ 事实和理由：{f7_fact}'
    thisCase.reasons.append(f7_detail)

    # 8. 对欠付物业费数额及计算方式有无异议
    st.subheader("8. 对欠付物业费数额及计算方式有无异议")
    f8_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="f8_options", horizontal=True)
    if f8_options == "无":
        f8_detail = f'无☑\n有☐ 事实和理由：'
    else:
        f8_fact = st.text_area("事实和理由", key="f8_fact")
        ai_component.ai_optimize_text(
            f8_fact, id="f8_fact_b", isDefendant=True)
        f8_detail = f'无☐\n有☑ 事实和理由：{f8_fact}'
    thisCase.reasons.append(f8_detail)

    # 9. 对应付违约金数额及计算方式有无异议
    st.subheader("9. 对应付违约金数额及计算方式有无异议")
    f9_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="f9_options", horizontal=True)
    if f9_options == "无":
        f9_detail = f'无☑\n有☐ 事实和理由：'
    else:
        f9_fact = st.text_area("事实和理由", key="f9_fact")
        ai_component.ai_optimize_text(
            f9_fact, id="f9_fact_b", isDefendant=True)
        f9_detail = f'无☐\n有☑ 事实和理由：{f9_fact}'
    thisCase.reasons.append(f9_detail)

    # 10. 对催缴情况有无异议
    st.subheader("10. 对催缴情况有无异议")
    f10_options = st.radio(
        label='No label', label_visibility='collapsed', options=["无", "有"], key="f10_options", horizontal=True)
    if f10_options == "无":
        f10_detail = f'无☑\n有☐ 事实和理由：'
    else:
        f10_fact = st.text_area("事实和理由", key="f10_fact")
        ai_component.ai_optimize_text(
            f10_fact, id="f10_fact_b", isDefendant=True)
        f10_detail = f'无☐\n有☑ 事实和理由：{f10_fact}'
    thisCase.reasons.append(f10_detail)

    # 11. 其他需要说明的内容
    st.subheader("11. 其他需要说明的内容（可另附页）")
    f11_content = st.text_area("其他内容", key="f11_content")
    ai_component.ai_optimize_text(
        f11_content, id="f11_content_b", isDefendant=True)
    thisCase.reasons.append(f11_content)

    # 12. 证据清单
    st.subheader("12. 证据清单（可另附页）")
    f12_content = st.text_area("证据清单", key="f12_content")
    thisCase.reasons.append(f12_content)


class PropertyServiceCaseFormatter(BaseCaseFormatter):
    """数据格式化器"""

    BaseCaseFormatter.case_type = CASE_TYPE
    BaseCaseFormatter.isComplaint = False

    @staticmethod
    def format_case(case):
        """将案件对象转换为适合文档模板的格式"""
        case_data = json.loads(case.to_json())

        # 调用父类的通用格式化方法
        template_data = super(PropertyServiceCaseFormatter,
                              PropertyServiceCaseFormatter).format_case(case)

        # 添加案件的自定义部分
        template_data.update({
            "reply_matters": PropertyServiceCaseFormatter._format_reply_matters(case_data), "case_num": case_data.get("case_num", "")
        })
        template_data.update(
            {"reasons": PropertyServiceCaseFormatter._format_reasons(case_data)})

        return template_data

    @staticmethod
    def _format_reply_matters(case_data):
        """Format reply matters from the case data"""
        reply_matters = case_data.get('reply_matters', [])

        matter_types = [
            "1. 对物业费有无异议",
            "2. 对违约金有无异议",
            "3. 对其他请求有无异议",
            "4. 对标的总额有无异议",
            "5. 答辩依据"
        ]

        formatted_matters = []

        for i, matter_type in enumerate(matter_types):
            if i < len(reply_matters):
                formatted_matters.append({
                    "type": matter_type,
                    "information": reply_matters[i]
                })
            else:
                formatted_matters.append({
                    "type": matter_type,
                    "information": ""
                })

        return formatted_matters

    @staticmethod
    def _format_reasons(case_data):
        """Format reasons from the case data"""
        reasons = case_data.get('reasons', [])

        reason_types = [
            "1. 对物业服务合同或前期物业服务合同签订情况（名称、编号、签订时间、地点等）有无异议",
            "2. 对签订主体有无异议",
            "3. 对物业项目情况有无异议",
            "4. 对物业费标准有无异议",
            "5. 对物业服务期限有无异议",
            "6. 对物业费支付方式有无异议",
            "7. 对逾期支付物业费违约金标准有无异议",
            "8. 对欠付物业费数额及计算方式有无异议",
            "9. 对应付违约金数额及计算方式有无异议",
            "10. 对催缴情况有无异议",
            "11. 其他需要说明的内容（可另附页）",
            "12. 证据清单（可另附页）"
        ]

        formatted_reasons = []

        for i, reason_type in enumerate(reason_types):
            if i < len(reasons):
                formatted_reasons.append({
                    "type": reason_type,
                    "information": reasons[i]
                })
            else:
                formatted_reasons.append({
                    "type": reason_type,
                    "information": ""
                })

        return formatted_reasons


class PropertyServiceCaseRespondent:
    def __init__(self):
        self.respondent = None
        self.case_num = None
        self.reply_matters = []
        self.reasons = []

    def to_json(self):
        def default_serializer(obj):
            if isinstance(obj, date):
                return obj.isoformat()
            elif hasattr(obj, '__dict__'):
                return obj.__dict__
            elif isinstance(obj, pd.DataFrame):
                return obj.to_dict(orient='records')
            else:
                return str(obj)

        return json.dumps(self.__dict__, default=default_serializer, indent=4)


thisCase = PropertyServiceCaseRespondent()

header(CASE_TYPE, "答辩状")

st.markdown("""______""")
st.subheader('案号')
thisCase.case_num = st.text_input(
    '请输入案号：', '', placeholder='示例：(2025)粤01民终0001号')
st.header("当事人信息")
respondent = Respondent(CASE_TYPE)
respondent.show()
thisCase.respondent = respondent
st.markdown("""______""")
st.header("答辩事项和依据（对原告诉讼请求的确认或者异议）")
respondent_details(thisCase)
st.header("事实和理由（对起诉状事实与理由的确认或者异议）")
fact_reason(thisCase)

if st.button("生成答辩状"):

    try:
        with st.spinner("生成中..."):
            doc_bytes, filename,preview = DocumentGenerator.generate_document(
                "defense",
                thisCase,
                PropertyServiceCaseFormatter,
                thisCase.respondent.respondents[0]["name"],
            )
        with st.expander("预览"):
            st.markdown(preview, unsafe_allow_html=True)
        st.download_button(
            label="下载答辩状",
            data=doc_bytes,
            file_name=filename,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    except Exception as e:
        st.error(f"生成文档时出错: {str(e)}")
