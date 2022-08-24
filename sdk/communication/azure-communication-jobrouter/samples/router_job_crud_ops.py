# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: router_job_crud_ops.py
DESCRIPTION:
    These samples demonstrates how to create Job used in ACS JobRouter.
    You need a valid connection string to an Azure Communication Service to execute the sample

USAGE:
    python router_job_crud_ops.py
    Set the environment variables with your own values before running the sample:
    1) AZURE_COMMUNICATION_SERVICE_ENDPOINT - Communication Service endpoint url
"""

import os
import time


class RouterJobSamples(object):
    endpoint = os.environ.get("AZURE_COMMUNICATION_SERVICE_ENDPOINT", None)
    if not endpoint:
        raise ValueError("Set AZURE_COMMUNICATION_SERVICE_ENDPOINT env before run this sample.")

    _job_id = "sample_job"
    _job_w_cp_id = "sample_job_w_cp"
    _distribution_policy_id = "sample_distribution_policy"
    _classification_policy_id = "sample_classification_policy"
    _queue_id = "sample_queue"
    _worker_id = "sample_worker"

    def setup_distribution_policy(self):
        connection_string = self.endpoint
        distribution_policy_id = self._distribution_policy_id

        from azure.communication.jobrouter import (
            RouterAdministrationClient,
            LongestIdleMode
        )

        router_admin_client = RouterAdministrationClient.from_connection_string(conn_str = connection_string)
        print("RouterAdministrationClient created successfully!")

        dist_policy = router_admin_client.create_distribution_policy(
            distribution_policy_id = distribution_policy_id,
            offer_ttl_seconds = 10 * 60,
            mode = LongestIdleMode(
                min_concurrent_offers = 1,
                max_concurrent_offers = 1
            )
        )

    def setup_queue(self):
        connection_string = self.endpoint
        queue_id = self._queue_id

        from azure.communication.jobrouter import (
            RouterAdministrationClient,
            JobQueue
        )

        router_admin_client = RouterAdministrationClient.from_connection_string(conn_str = connection_string)

        job_queue = router_admin_client.create_queue(
            queue_id = queue_id,
            distribution_policy_id = self._distribution_policy_id
        )

    def setup_classification_policy(self):
        connection_string = self.endpoint
        classification_policy_id = self._distribution_policy_id

        from azure.communication.jobrouter import (
            RouterAdministrationClient,
            StaticRule,
            StaticQueueSelectorAttachment,
            QueueSelector,
            LabelOperator
        )

        router_admin_client = RouterAdministrationClient.from_connection_string(conn_str = connection_string)
        print("RouterAdministrationClient created successfully!")

        classification_policy = router_admin_client.create_classification_policy(
            classification_policy_id = classification_policy_id,
            prioritization_rule = StaticRule(value = 10),
            queue_selectors = [
                StaticQueueSelectorAttachment(
                    label_selector = QueueSelector(
                        key = "Id",
                        label_operator = LabelOperator.EQUAL,
                        value = self._queue_id)
                )
            ]
        )

    def setup_worker(self):
        connection_string = self.endpoint
        worker_id = self._worker_id
        queue_id = self._queue_id

        from azure.communication.jobrouter import (
            RouterClient,
            ChannelConfiguration,
            QueueAssignment
        )

        router_client = RouterClient.from_connection_string(conn_str = connection_string)
        router_worker = router_client.create_worker(
            worker_id = worker_id,
            total_capacity = 100,
            available_for_offers = True,
            channel_configurations = {
                "general": ChannelConfiguration(capacity_cost_per_job = 100)
            },
            queue_assignments = {
                queue_id: QueueAssignment()
            }
        )

    def create_job(self):
        connection_string = self.endpoint
        job_id = self._job_id
        job_w_cp_id = self._job_w_cp_id
        queue_id = self._queue_id
        classification_policy_id = self._classification_policy_id

        # [START create_job]
        from azure.communication.jobrouter import (
            RouterClient,
        )

        # set `connection_string` to an existing ACS endpoint
        router_client = RouterClient.from_connection_string(conn_str = connection_string)
        print("RouterAdministrationClient created successfully!")

        # We need to create a distribution policy + queue as a pre-requisite to start creating job
        router_job = router_client.create_job(
            job_id = job_id,
            channel_id = "general",
            queue_id = queue_id,
            priority = 10,
            channel_reference = "12345"
        )

        print(f"Job has been successfully created with status: {router_job.job_status}")

        # Alternatively, a job can also be created while specifying a classification policy
        # As a pre-requisite, we would need to create a classification policy first
        router_job_with_cp = router_client.create_job(
            job_id = job_w_cp_id,
            channel_id = "general",
            classification_policy_id = classification_policy_id,
            channel_reference = "12345"
        )
        print(f"Job has been successfully created with status: {router_job_with_cp.job_status}")

        # [END create_job]

    def update_job(self):
        connection_string = self.endpoint
        job_id = self._job_id
        # [START update_job]
        from azure.communication.jobrouter import (
            RouterClient,
            RouterWorker,
            QueueAssignment,
            ChannelConfiguration,
        )

        # set `connection_string` to an existing ACS endpoint
        router_client: RouterClient = RouterClient.from_connection_string(conn_str = connection_string)
        print("RouterAdministrationClient created successfully!")

        update_job = router_client.update_job(
            job_id = job_id,
            channel_reference = "45678"
        )

        print(f"Job has been successfully update with channel reference: {update_job.channel_reference}")
        # [END update_job]

    def get_job(self):
        connection_string = self.endpoint
        job_id = self._job_id
        # [START get_job]
        from azure.communication.jobrouter import RouterClient

        router_client = RouterClient.from_connection_string(conn_str = connection_string)

        router_job = router_client.get_job(job_id = job_id)

        print(f"Successfully fetched router worker with id: {router_job.id}")
        # [END get_job]

    def get_job_position(self):
        connection_string = self.endpoint
        job_id = self._job_id
        # [START get_job_position]
        from azure.communication.jobrouter import RouterClient

        router_client = RouterClient.from_connection_string(conn_str = connection_string)

        router_job_position = router_client.get_queue_position(job_id = job_id)

        print(f"Successfully fetched router job position: {router_job_position.position}")
        # [END get_job_position]

    def reclassify_job(self):
        connection_string = self.endpoint
        job_id = self._job_w_cp_id
        # [START reclassify_job]
        from azure.communication.jobrouter import RouterClient

        router_client = RouterClient.from_connection_string(conn_str = connection_string)

        reclassify_job_result = router_client.reclassify_job(job_id = job_id)

        print(f"Successfully re-classified router")
        # [END reclassify_job]

    def accept_job_offer(self):
        connection_string = self.endpoint
        job_id = self._job_id
        worker_id = self._worker_id

        from azure.communication.jobrouter import (
            RouterClient,
            JobOffer
        )

        router_client = RouterClient.from_connection_string(conn_str = connection_string)

        while any(
                [offer for offer in (router_client.get_worker(worker_id = worker_id)).offers if
                 offer.job_id != job_id]):
            time.sleep(secs = 1)

        queried_worker = router_client.get_worker(worker_id = worker_id)
        issued_offer: JobOffer = [offer for offer in queried_worker.offers if offer.job_id == job_id][0]
        offer_id = issued_offer.id

        # [START accept_job_offer]
        from azure.communication.jobrouter import (
            RouterJob,
            AcceptJobOfferResult
        )

        accept_job_offer_result: AcceptJobOfferResult = router_client.accept_job_offer(
            worker_id = worker_id,
            offer_id = offer_id
        )

        queried_job: RouterJob = router_client.get_job(job_id = job_id)

        print(f"Job has been successfully assigned to worker. Current job status: {queried_job.job_status}")
        print(f"Job has been successfully assigned with a worker with assignment "
              f"id: {accept_job_offer_result.assignment_id}")
        # [END accept_job_offer]

        try:
            # [START decline_job_offer]
            decline_job_offer_result = router_client.decline_job_offer(
                worker_id = worker_id,
                offer_id = offer_id
            )
            # [END decline_job_offer]
        except Exception:
            print(f"Error encountered")

    def complete_and_close_job(self):
        connection_string = self.endpoint
        job_id = self._job_id

        # [START complete_job]
        from azure.communication.jobrouter import (
            RouterClient,
            RouterJob,
            CompleteJobResult,
            CloseJobResult
        )

        router_client = RouterClient.from_connection_string(conn_str = connection_string)

        queried_job: RouterJob = router_client.get_job(job_id = job_id)

        assignment_id = [k for k, v in queried_job.assignments.items()][0]

        complete_job_result: CompleteJobResult = router_client.complete_job(
            job_id = job_id,
            assignment_id = assignment_id
        )

        queried_job: RouterJob = router_client.get_job(job_id = job_id)

        print(f"Job has been successfully completed. Current status: {queried_job.job_status}")
        # [END complete_job]

        # [START close_job]
        close_job_result: CloseJobResult = router_client.close_job(
            job_id = job_id,
            assignment_id = assignment_id
        )

        queried_job: RouterJob = router_client.get_job(job_id = job_id)

        print(f"Job has been successfully closed. Current status: {queried_job.job_status}")

        # [END close_job]

    def list_jobs(self):
        connection_string = self.endpoint
        # [START list_jobs]
        from azure.communication.jobrouter import RouterClient

        router_client = RouterClient.from_connection_string(conn_str = connection_string)

        router_job_iterator = router_client.list_jobs(results_per_page = 10)

        for job_page in router_job_iterator.by_page():
            jobs_in_page = list(job_page)
            print(f"Retrieved {len(jobs_in_page)} jobs in current page")

            for j in jobs_in_page:
                print(f"Retrieved job with id: {j.router_job.id}")

        print(f"Successfully completed fetching jobs")
        # [END list_jobs]

    def cancel_job(self):
        connection_string = self.endpoint
        job_id = self._job_w_cp_id

        # [START cancel_job]
        from azure.communication.jobrouter import RouterClient

        router_client = RouterClient.from_connection_string(conn_str = connection_string)

        router_client.delete_job(job_id = job_id)

        # [END cancel_job]

    def clean_up(self):
        connection_string = self.endpoint
        job_id = self._job_id

        # [START delete_job]
        from azure.communication.jobrouter import RouterClient

        router_client = RouterClient.from_connection_string(conn_str = connection_string)

        router_client.delete_job(job_id = job_id)

        # [END delete_job]


if __name__ == '__main__':
    sample = RouterJobSamples()
    sample.setup_distribution_policy()
    sample.setup_queue()
    sample.setup_classification_policy()
    sample.setup_worker()
    sample.create_job()
    sample.get_job()
    sample.get_job_position()
    sample.update_job()
    sample.reclassify_job()
    sample.accept_job_offer()
    sample.complete_and_close_job()
    sample.list_jobs()
    sample.clean_up()
