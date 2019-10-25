---
---

# Current steering council
The current steering council is the only official group of people attached to
the Jupyter Project. It consists of 21 members listed here:

https://jupyter.org/about

This team has grown iteratively since the beginning of the Jupyter Project.

For the sake of clarity, references to "the new steering council" refers to
the organizing body that replaces the current steering council.

It also assumes that we use a Jupyter Enhancement Proposal (JEP) process
for proposing and making decisions. This post will not detail the JEP process,
because [Safia already did a great job of this here](https://github.com/jupyter/enhancement-proposals/issues/27).
It also assumes that *this* document is written in the form of a JEP, similar to
what the Python community used.

# The steering council
## Composition
The steering council is a 5-person committee.

## Mandate
The steering council shall work to:

Maintain the quality and stability of the Jupyter core projects,
Make contributing as accessible, inclusive, and sustainable as possible,
Formalize and maintain the relationship between the core team and NumFocus,
Establish appropriate decision-making processes for teams in the Jupyter community,
Seek consensus among contributors and the core team before acting in a formal capacity,
Act as a "court of final appeal" for decisions where all other methods have failed.

## Powers
The council has broad authority to make decisions about the project. For example, they can:

Accept or reject JEPs and PRs
Enforce or update the project's code of conduct
Work with NumFocus to manage any project assets
Delegate parts of their authority to other subcommittees or processes
However, they cannot modify this JEP, or affect the membership of the core team, except via the mechanisms specified in this document.

The council should look for ways to use these powers as little as possible. Instead of voting, it's better to seek consensus. Instead of ruling on individual JEPs, it's better to define a standard process for JEP decision making (for example, by formalizing [the meta-JEP process recently proposed](https://github.com/jupyter/enhancement-proposals/tree/master/29-jep-process)).
It's better to establish a Code of Conduct committee than to rule on individual cases. And so on.

To use its powers, the council votes. Every council member must either vote or explicitly abstain. Members with conflicts of interest on a particular vote must abstain. Passing requires a strict majority of non-abstaining council members.

Whenever possible, the council's deliberations and votes shall be held in public.

## Electing the council
A council election consists of two phases:

Phase 1: Candidates advertise their interest in serving. Candidates must be nominated by a core team member. Self-nominations are allowed.
Phase 2: Each core team member can vote for zero or more of the candidates. Voting is performed anonymously. Candidates are ranked by the total number of votes they receive. If a tie occurs, it may be resolved by mutual agreement among the candidates, or else the winner will be chosen at random.
Each phase lasts one to two weeks, at the outgoing council's discretion. For the initial election, both phases will last two weeks.

The election process is managed by [a returns officer](https://en.wikipedia.org/wiki/Returning_officer) nominated by the outgoing steering council. For the initial election, the returns officer will be nominated by the Brian Granger and Fernando Perez.

The council should ideally reflect the diversity of Jupyter contributors and users, and core team members are encouraged to vote accordingly.

## Term

Jupyter will define a cycle of operations, roughly mapping onto a "major version release cycle"
if it were a single project. The details of what this means will be decided by the
steering council and the JEP process.

A new council is elected after cycle. Each council's term runs from when their election results are finalized until the next council's term starts. There are no term limits.

## Vacancies
Council members may resign their position at any time.

Whenever there is a vacancy during the regular council term, the council may vote to appoint a replacement to serve out the rest of the term.

If a council member drops out of touch and cannot be contacted for a month or longer, then the rest of the council may vote to replace them.

## Conflicts of interest
While we trust council members to act in the best interests of Jupyter rather than themselves or their employers, the mere appearance of any one company dominating Jupyter development could itself be harmful and erode trust. In order to avoid any appearance of conflict of interest, at most 2 members of the council can work for any single employer.

In a council election, if 3 of the top 5 vote-getters work for the same employer, then whichever of them ranked lowest is disqualified and the 6th-ranking candidate moves up into 5th place; this is repeated until a valid council is formed.

During a council term, if changing circumstances cause this rule to be broken (for instance, due to a council member changing employment), then one or more council members must resign to remedy the issue, and the resulting vacancies can then be filled as normal.

## Ejecting core team members
In exceptional circumstances, it may be necessary to remove someone from the core team against their will. (For example: egregious and ongoing code of conduct violations.) This can be accomplished by a steering council vote, but unlike other steering council votes, this requires at least a two-thirds majority. With 5 members voting, this means that a 3:2 vote is insufficient; 4:1 in favor is the minimum required for such a vote to succeed. In addition, this is the one power of the steering council which cannot be delegated, and this power cannot be used while a vote of no confidence is in process.

If the ejected core team member is also on the steering council, then they are removed from the steering council as well.

## Vote of no confidence
In exceptional circumstances, the core team may remove a sitting council member, or the entire council, via a vote of no confidence.

A no-confidence vote is triggered when a core team member calls for one publically on an appropriate project communication channel, and another core team member seconds the proposal.

The vote lasts for two weeks. Core team members vote for or against. If at least two thirds of voters express a lack of confidence, then the vote succeeds.

There are two forms of no-confidence votes: those targeting a single member, and those targeting the council as a whole. The initial call for a no-confidence vote must specify which type is intended. If a single-member vote succeeds, then that member is removed from the council and the resulting vacancy can be handled in the usual way. If a whole-council vote succeeds, the council is dissolved and a new council election is triggered immediately.

# The core team
## Role
The core team is the group of trusted volunteers who manage Jupyter. They assume many roles required to achieve the project's goals, especially those that require a high level of trust. They make the decisions that shape the future of the project.

Core team members are expected to act as role models for the community and custodians of the project, on behalf of the community and all those who rely on Jupyter.

They will intervene, where necessary, in online discussions or at official Jupyter events on the rare occasions that a situation arises that requires intervention.

They have authority over the Jupyter Project infrastructure, including the jupyter.org website itself, the "core Jupyter GitHub organizations and repositories", the community forum, the mailing lists, Gitter channels,
and any cloud infrastructure such as nbconvert, mybinder.org, etc.

## Prerogatives
Core team members may participate in formal votes, typically to nominate new team members and to elect the steering council.

## Membership
Jupyter core team members demonstrate:

a good grasp of the philosophy of the Jupyter Project
a solid track record of being constructive and helpful
significant contributions to the project's goals, in any form
willingness to dedicate some time to improving Jupyter
As the project matures, contributions go beyond code. Here's an incomplete list of areas where contributions may be considered for joining the core team, in no particular order:

Working on community management and outreach
Providing support on the mailing lists, gitter rooms, and the community forum
Triaging tickets
Writing patches (code, docs, or tests)
Reviewing patches (code, docs, or tests)
Participating in design decisions
Providing expertise in a particular domain (security, i18n, etc.)
Managing the continuous integration infrastructure
Managing the servers (website, tracker, documentation, etc.)
Maintaining related projects (alternative interpreters, core infrastructure like packaging, etc.)
Creating visual designs
Core team membership acknowledges sustained and valuable efforts that align well with the philosophy and the goals of the Jupyter project.

It is granted by receiving at least two-thirds positive votes in a core team vote that is open for one week and with no veto by the steering council.

Core team members are always looking for promising contributors, teaching them how the project is managed, and submitting their names to the core team's vote when they're ready.

There's no time limit on core team membership. However, in order to provide the general public with a reasonable idea of how many people maintain Jupyter, core team members who have stopped contributing are encouraged to declare themselves as "inactive". Those who haven't made any non-trivial contribution in two years may be asked to move themselves to this category, and moved there if they don't respond. To record and honor their contributions, inactive team members will continue to be listed alongside active core team members; and, if they later resume contributing, they can switch back to active status at will. While someone is in inactive status, though, they lose their active privileges like voting or nominating for the steering council, and commit access.

The initial active core team members will consist of everyone with commit access to one of the Jupyter core repositories on Github.

# Changing this document
Changes to this document require at least a two-thirds majority of votes cast in a core team vote which should be open for two weeks.