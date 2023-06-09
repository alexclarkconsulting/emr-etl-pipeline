import aws_cdk as core
import aws_cdk.assertions as assertions

from emr_etl_pipeline.emr_etl_pipeline_stack import EmrEtlPipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in emr_etl_pipeline/emr_etl_pipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EmrEtlPipelineStack(app, "emr-etl-pipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
